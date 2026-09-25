# Opus 5.5 website rebuilds

Seven websites rebuilt in plain HTML, CSS and JavaScript from a screen recording.

## Credit

The original sites come from the YouTube video
[NEW Opus 5.5 is INSANE at Building Websites (Full Showcase)](https://www.youtube.com/watch?v=mPiaap4zEVk)
by **Brendan Jowett** ([@brendanautomation](https://www.youtube.com/@brendanautomation)).
In that video, Claude Opus 5.5 builds seven sites from scratch. The designs, layouts,
animations and brand names are from that video. This repository is not affiliated with
Brendan Jowett or Anthropic.

## What is in this repository

| Folder | Site | Notes |
|---|---|---|
| `sites/1-hotel` | Solenne, cliffside hotel | room carousel, day-cycle clock, booking calendar |
| `sites/2-festival` | SALTHOWL, music festival | timetable with clash detection, festival map |
| `sites/3-ecommerce` | KALDER, clothing brand | pinned lookbook with hotspots, shipping map |
| `sites/4-saas` | Kestrel, finance SaaS | live coded dashboard, ROI calculator |
| `sites/5-drink` | HYPERLYTE, sports drink | three.js can built in code |
| `sites/6-highrise` | HALDEN, residential tower | procedural three.js tower and city |
| `sites/7-space` | KÁRMÁN, space tourism | procedural rocket, Earth shader, Moon pass |

Open any `sites/<N-name>/index.html` in a browser. There is no build step.
The pages load Google Fonts and scripts from cdnjs / jsDelivr.

## How it was made

1. Claude Opus 5.5 agents rebuilt each site from video frames, one agent per site.
   `BRIEF.md` is the brief they followed.
2. At first the photos were cropped from the video. All 75 photos were then replaced
   with new images generated from text prompts (GPT Image 2.5 through Higgsfield).
   No photo in `sites/*/img/` comes from the video.
3. The page text was first copied from the video. It was then rewritten in new words.
   Only the seven brand names are kept.
4. The top banner of each page links to the source video. The original banners showed
   the build time and API cost of the original build. Those numbers are removed,
   because they do not describe these rebuilds.

## Scripts

- `scripts/shot.py <html> <outdir> [scrollY ...]` takes Chrome screenshots (Playwright)
  and prints the page height and JS errors.
- `scripts/evidence.py` and `scripts/evidence_page.py` build a comparison report:
  video frame against rebuild, with and without the photos.
- `scripts/cmp.py` and `scripts/sheets.py` need video frames, which are not in this repository.

No license is set.
