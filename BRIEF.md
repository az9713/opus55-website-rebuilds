# Brief for each site-rebuild agent

Project root: `C:\Users\<user>\Downloads\opus5.5_website_brendan` (use Git Bash paths `/c/Users/<user>/Downloads/opus5.5_website_brendan`).

Goal: recreate ONE website shown in a YouTube screen recording, with the highest visual fidelity to the original, including its animations. The original sites were built by Claude Opus 5.5 with GPT-image photos.

## Inputs
- `frames/<site>/f_NNNN.jpg` — 2560x1440 frames at 2 fps. Frame n = video time (segment start + n/2 s). The segment may include a few seconds of the previous/next site at its edges — ignore those.
- `sheets/<site>/sheet_XX.jpg` — contact sheets, 20 frames each (every 2nd frame = 1 fps), labeled with the frame file name. READ THE SHEETS FIRST to map sections to frame ranges. Then read full frames only where you need copy text, layout detail, or colors (about 20–40 full frames). Do not read every frame.
- `transcript.txt` — narration; find your chapter. It names the animations the presenter points out.
- To see motion in detail, extract a short high-fps window yourself, e.g.
  `"/c/Users/<user>/AppData/Local/Programs/Python/Python313/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe" -loglevel error -ss <sec> -t 2 -i video/source.webm -vf fps=10 scratch/<site>/m_%03d.jpg`
  Put scratch files under `scratch/<site>/`, never elsewhere.

## Frame geometry
- The browser viewport in each frame is roughly x 0–2545, y 87–1354 (2560x1440 frame). Above is black; the site's own top banner starts at y≈87.
- A webcam picture-in-picture of the presenter covers the bottom-left (~x 0–545, y 1045–1440) in many frames. Content under it is unrecoverable unless another frame shows it. Do not reproduce the webcam.
- The site includes a pinned top banner "Built by Claude Opus 5.5 | BUILD TIME | TOKENS | API COST". It is part of the page: recreate it with the exact numbers seen in your frames.

## Output
- `sites/<site>/index.html` — self-contained (inline CSS/JS). Allowed external: Google Fonts; scripts from cdnjs.cloudflare.com or cdn.jsdelivr.net/npm (e.g. three.js, GSAP + ScrollTrigger, Lenis). No downloaded 3D models: build 3D from code (procedural geometry, canvas textures), same as the original constraint.
- `sites/<site>/img/` — images. Policy: crop photos directly from the frames with Python PIL (the clearest, unobscured frame; crop the photo area only, no UI text over it where avoidable; save as .jpg quality 90). Where a photo is always covered by text or the webcam, crop what you can, or use a CSS gradient that matches its colors. Do not call any paid image API.
- Match: fonts (identify by eye, pick nearest Google Font), exact colors (sample pixels from frames with PIL), copy text (verbatim wherever readable), layout, spacing, section order, and every interaction/animation seen or narrated (load-in, scroll reveals, parallax, hovers, carousels, modals, pinned scroll scenes, 3D, counters, etc.).
- Interactive features seen in the video (filters, calculators, schedule pickers, modals, flavor switchers, floor selectors) must work.

## Verify
- Screenshot your page: `python scripts/shot.py sites/<site>/index.html scratch/<site>/shots 0 800 1600 ...` (viewport 1600x792 CSS px, output 2560 wide = same scale as frames). It prints page height and JS errors.
- Compare your screenshots against matching frames by viewing both. Fix differences. Iterate at least twice. Zero JS errors.

## Report back (short)
1. File path and page height.
2. Sections built, in order.
3. Animations/interactions built.
4. What differs from the original and why (unreadable text, hidden by webcam, approximated font, image quality, etc.).
5. Frame numbers you used as reference for the hero and 2 other sections (the main thread will spot-check).
