---
name: social-post
description: Write platform-specific publishing fields for YouTube, YouTube Shorts, TikTok, Instagram, X, and LinkedIn with checked limits, audience-focused hooks, descriptions, tags, hashtags, accessibility text, and measurable marketing goals. Use when preparing social copy or a multi-platform content package.
license: MIT
---

# Social Post

Create ready-to-paste copy for the requested networks. Adapt the message to each surface rather than copying one caption everywhere. Preparing content does not authorize posting it.

## Workflow

1. Collect the actual content or transcript, audience, language, goal, brand voice, offer, supported facts, call to action, links, target networks, and whether the surface is organic or paid. Ask only for missing decisive inputs.
2. Read [the platform fields and limits](references/platforms.md) for each selected surface. Recheck volatile limits against official documentation and the actual publishing interface before final delivery. Distinguish app, API, account tier, and ad-product restrictions.
3. Apply [the marketing procedure](references/marketing.md). Select one central audience benefit, an accurate hook, supporting evidence, and one primary action. Do not invent testimonials, results, urgency, links, timestamps, or product features.
4. Fill the fields in [the output template](assets/post-package.md). Use actual native fields. Label optional supporting copy separately when a network has no native title, tag, or description field.
5. Count the final text including hashtags, spaces, newlines, mentions, disclosure, and links. Use `python3 scripts/count-fields.py --help` for Unicode, UTF-8, UTF-16, and YouTube tag counts. For X, use its weighted parser as documented in [validation](references/validation.md), not a raw string length.
6. Read the copy as a user would see it before truncation. Verify spelling, facts, links, accessibility text, selected publishing settings, and field counts. Keep strategic recommendations distinct from hard limits.
7. Deliver the finished fields, count/limit table, recommended variant, reason for its fit, and a small measurement plan. Mark only genuinely unavailable fields as not applicable. Provide all requested platform packages.

Do not call a placeholder-filled draft ready to publish. If a source fact or destination link is missing, complete independent copy and identify the precise remaining input. Consult [source notes](references/sources.md) for verification dates and unresolved platform conflicts.

## License

[MIT license and copyright notice](LICENSE.md).
