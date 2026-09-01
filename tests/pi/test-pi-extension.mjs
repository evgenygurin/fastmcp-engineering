import { pathToFileURL } from 'url';
import { mkdtempSync, rmSync, mkdirSync, writeFileSync } from 'fs';
import { tmpdir } from 'os';
import { join } from 'path';

const extensionPath = process.argv[2];
if (!extensionPath) {
  console.error('Usage: node test-pi-extension.mjs EXTENSION_PATH');
  process.exit(2);
}

const tmp = mkdtempSync(join(tmpdir(), 'pi-test-'));
const skillsDir = join(tmp, 'skills');
mkdirSync(join(skillsDir, 'using-fastmcp-engineering'), { recursive: true });
writeFileSync(
  join(skillsDir, 'using-fastmcp-engineering', 'SKILL.md'),
  '---\nname: using-fastmcp-engineering\ndescription: test\n---\n\n# Bootstrap body\n',
  'utf8'
);

const handlers = {};
const api = {
  on(name, fn) { handlers[name] = fn; },
};

const mod = await import(pathToFileURL(extensionPath).href);
const ext = mod.default(api);

// resources_discover registers skills
const discovered = await handlers.resources_discover();
if (!discovered.skillPaths || !discovered.skillPaths.some(p => p.includes('skills'))) {
  console.error('FAIL: resources_discover did not register skills path');
  process.exit(1);
}
console.log('PASS: resources_discover registers skills path');

// context event injects bootstrap once
const makeMessages = (n = 1) => Array.from({ length: n }, (_, i) => ({
  role: 'user',
  content: [{ type: 'text', text: `message ${i}` }],
}));

let messages = makeMessages();
let result = await handlers.context({ messages });
if (!result || !result.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  console.error('FAIL: bootstrap not injected');
  process.exit(1);
}
const injected = result.messages.filter(m => JSON.stringify(m).includes('fastmcp-engineering')).length;
if (injected !== 1) {
  console.error(`FAIL: expected 1 bootstrap message, got ${injected}`);
  process.exit(1);
}
console.log('PASS: bootstrap injected once');

// dedup: after injection, context event must not re-inject
messages = result.messages;
result = await handlers.context({ messages });
if (result && result.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  // dedup via marker: no new injection
  const count = result.messages.filter(m => JSON.stringify(m).includes('fastmcp-engineering')).length;
  if (count > 1) {
    console.error(`FAIL: dedup failed, ${count} bootstrap messages`);
    process.exit(1);
  }
}
console.log('PASS: dedup guard works');

// compaction: agent_end clears flag, session_start re-arms
handlers.agent_end();
let result2 = await handlers.context({ messages: makeMessages() });
if (result2 && result2.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  console.error('FAIL: bootstrap injected after agent_end');
  process.exit(1);
}
handlers.session_start();
result2 = await handlers.context({ messages: makeMessages() });
if (!result2 || !result2.messages.some(m => JSON.stringify(m).includes('fastmcp-engineering'))) {
  console.error('FAIL: bootstrap not re-injected after session_start');
  process.exit(1);
}
console.log('PASS: compaction/lifecycle re-injection works');

rmSync(tmp, { recursive: true, force: true });
console.log('\nAll pi extension tests passed.');
