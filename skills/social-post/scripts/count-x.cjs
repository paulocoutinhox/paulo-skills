#!/usr/bin/env node
const fs = require('node:fs');
const twitterText = require('twitter-text');

if (process.argv.length !== 3) {
  process.stderr.write('Usage: node scripts/count-x.cjs <utf8-text-file>\n');
  process.exit(2);
}

try {
  const content = fs.readFileSync(process.argv[2], 'utf8');
  const result = twitterText.parseTweet(content);

  process.stdout.write(JSON.stringify({
    unit: 'x-weighted',
    count: result.weightedLength,
    limit: 280,
    valid: result.valid,
  }) + '\n');

  process.exit(result.valid ? 0 : 1);
} catch (error) {
  process.stderr.write(`Cannot validate the input: ${error.message}\n`);
  process.exit(2);
}
