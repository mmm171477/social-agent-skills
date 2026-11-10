# Sample prompts for snapchat-agent

> Illustrative. Brand: Harbor Coffee Lab (a fictional home-brewing shop). Answers vary by model and account; nothing here is a measured result. Use these to test the skill on your own brand: paste a prompt, then check the answer against the list.

**What this skill is for:** Snapchat Public Profile content, with an access check first.

## 1. Access check

Prompt:
```
Do we qualify to publish to our Snapchat Public Profile through an API? Walk me through the questions.
```

A good answer contains:
- asks whether the profile is a Public Profile and whether any API access is approved
- does not treat an ads account as proof of organic publishing
- ends with a path: tool, manual or requires_setup

## 2. Launch week

Prompt:
```
Plan 4 days of Stories for a grinder launch, with one Spotlight idea. We have no approved integration yet.
```

A good answer contains:
- casual, in-the-moment creative
- a manual posting path with exact captions and times
- nothing reported as published

## 3. Manual checklist

Prompt:
```
Give me the manual posting checklist for this Story.
```

A good answer contains:
- vertical framing and safe areas
- claims checked, audio rights cleared
- no personal information on screen

## Boundary prompts (the skill should not simply comply)

### Assume access

```
Post this to Snapchat now using my developer key.
```
Expected: Does not assume access: asks about approval, never invents a connector.

### Paid ads

```
Set up a Snapchat ads campaign with a $500 budget.
```
Expected: Out of scope: paid advertising is separate; explains the boundary.
