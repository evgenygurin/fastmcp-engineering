import fs from 'fs';
import { pathToFileURL } from 'url';

const [, , pluginPath, scenario] = process.argv;

if (!pluginPath || !['present', 'missing'].includes(scenario)) {
  console.error('Usage: node test-bootstrap-caching.mjs PLUGIN_PATH present|missing');
  process.exit(2);
}

let existsCount = 0;
let readCount = 0;

const originalExistsSync = fs.existsSync;
const originalReadFileSync = fs.readFileSync;

fs.existsSync = function (...args) {
  if (isBootstrapSkillPath(args[0])) {
    existsCount += 1;
  }
  return originalExistsSync.apply(this, args);
};

fs.readFileSync = function (...args) {
  if (isBootstrapSkillPath(args[0])) {
    readCount += 1;
  }
  return originalReadFileSync.apply(this, args);
};

const mod = await import(pathToFileURL(pluginPath).href);
const plugin = await mod.FastMcpEngineeringPlugin({ client: {}, directory: '.' });
const transform = plugin['experimental.chat.messages.transform'];

const firstOutput = makeOutput(`${scenario} bootstrap first step`);
await transform({}, firstOutput);
const afterFirst = { existsCount, readCount };

const secondOutput = makeOutput(`${scenario} bootstrap second step`);
await transform({}, secondOutput);
const afterSecond = { existsCount, readCount };

const result = {
  scenario,
  firstBootstrapParts: countBootstrapParts(firstOutput),
  secondBootstrapParts: countBootstrapParts(secondOutput),
  mapsSubagentToTask: bootstrapText(firstOutput).includes('`task` with `subagent_type: "general"`'),
  mapsMutationToApplyPatch: bootstrapText(firstOutput).includes('`apply_patch`'),
  firstReadCount: afterFirst.readCount,
  secondReadCount: afterSecond.readCount,
  firstExistsCount: afterFirst.existsCount,
  secondExistsCount: afterSecond.existsCount,
};

const failures = scenario === 'present'
  ? assertPresentBootstrap(result)
  : assertMissingBootstrap(result);

if (failures.length > 0) {
  console.error(JSON.stringify(result, null, 2));
  for (const failure of failures) {
    console.error(`FAIL: ${failure}`);
  }
  process.exit(1);
}

console.log(JSON.stringify(result, null, 2));

function isBootstrapSkillPath(filePath) {
  return String(filePath).replaceAll('\\', '/').includes('using-fastmcp-engineering/SKILL.md');
}

function makeOutput(text) {
  return {
    messages: [{
      info: { role: 'user' },
      parts: [{ type: 'text', text }],
    }],
  };
}

function bootstrapText(output) {
  const parts = output.messages[0].parts;
  return parts.filter(p => p.type === 'text').map(p => p.text).join('\n');
}

function countBootstrapParts(output) {
  return bootstrapText(output).split('<EXTREMELY_IMPORTANT>').length - 1;
}

function assertPresentBootstrap(r) {
  const failures = [];
  if (r.firstBootstrapParts !== 1) failures.push(`expected 1 bootstrap in first output, got ${r.firstBootstrapParts}`);
  if (r.secondBootstrapParts !== 1) failures.push(`expected re-injection into fresh array (dedup guard only skips already-transformed arrays), got ${r.secondBootstrapParts}`);
  if (r.firstReadCount !== 1) failures.push(`expected 1 read of SKILL.md (cached), got ${r.firstReadCount}`);
  if (r.secondReadCount !== 1) failures.push(`expected no re-read after cache, got ${r.secondReadCount}`);
  if (!r.mapsSubagentToTask) failures.push('bootstrap missing subagent→task mapping');
  if (!r.mapsMutationToApplyPatch) failures.push('bootstrap missing edit→apply_patch mapping');
  return failures;
}

function assertMissingBootstrap(r) {
  const failures = [];
  if (r.firstBootstrapParts !== 0) failures.push(`expected 0 bootstrap when file missing, got ${r.firstBootstrapParts}`);
  if (r.secondBootstrapParts !== 0) failures.push(`expected 0 bootstrap when file missing, got ${r.secondBootstrapParts}`);
  return failures;
}
