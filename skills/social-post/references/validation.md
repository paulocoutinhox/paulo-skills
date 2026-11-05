# Text validation utilities

The Python utility has no external dependency. It reads a UTF-8 text file, preserves its exact newlines, prints counts, and returns a nonzero exit code when the explicitly selected limit is exceeded.

```bash
python3 scripts/count-fields.py caption.txt --unit utf16 --limit 2200
python3 scripts/count-fields.py description.txt --unit utf8 --limit 5000
python3 scripts/count-fields.py title.txt --unit codepoints --limit 100
python3 scripts/count-fields.py tags.json --unit youtube-tags --limit 500
```

`tags.json` must contain a JSON array of nonempty strings. YouTube tag accounting includes separating commas and two quote characters for each tag containing spaces. The script reports counts. It does not verify whether a tag is relevant or whether an account can publish the associated video. A UTF-16 count is a conservative check where a platform's character interpretation is unclear. It is not proof of platform acceptance.

## X weighted count

Use the actual parser instead of counting visible characters. Install its dependency in a temporary tool directory, not in the user's application unless requested:

```bash
npm install --prefix /tmp/social-post-tools --ignore-scripts --no-audit --no-fund twitter-text@3.1.0
NODE_PATH=/tmp/social-post-tools/node_modules node scripts/count-x.cjs post.txt
```

The script uses `twitter-text`'s `parseTweet`, reports weighted length and standard-post validity, and exits nonzero for invalid input. It does not validate premium account eligibility. Verify current parser and platform compatibility before relying on it operationally. If Node or the package is unavailable, state that weighted validation is pending rather than labeling an ordinary character count as exact.

The final count table should identify platform, field, unit, actual count, ceiling, and any interface-specific uncertainty. Count the final pasteable payload, including any trailing newline actually being pasted. Recheck after editing.
