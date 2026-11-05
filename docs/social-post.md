# Social Post

Prepare complete native publishing fields for the requested social networks.

## Invoke

Codex:

```text
$social-post Prepare copy for YouTube, Shorts, TikTok, Instagram, X, and LinkedIn from this transcript. The goal is qualified traffic to this product page.
```

Claude Code uses `/social-post` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Supply the actual content/transcript, audience, language, brand voice, goal, and destination link.
- Choose networks and exact surfaces, organic or paid.
- Provide only real claims, timestamps, mentions, offers, and required disclosures.

## What happens

The skill checks per-surface fields and limits, writes platform-specific copy, counts final payloads using the appropriate units, and verifies the opening, CTA, accessibility text, and supporting settings.

## Deliverables

Ready-to-paste fields for every selected platform, field/count/limit table, relevant alternatives, and a measurement hypothesis.

## Decisions and limits

YouTube Studio characters differ from API UTF-8 bytes. TikTok Direct Post uses UTF-16 accounting. X uses weighted parsing. Instagram account/API hashtag limits need live verification. A draft does not authorize posting.

## Detailed instructions

Read [the portable skill](../skills/social-post/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
