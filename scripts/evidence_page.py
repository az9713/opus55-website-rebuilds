# Writes evidence/index.html from evidence/meta.json.
import json, html
meta = json.load(open("evidence/meta.json"))
INFO = {
 "1-hotel": ("Solenne — luxury cliffside hotel", "1:05", "f_0030", "Loader, hero zoom, word-by-word text reveal, draggable room carousel, room modal, pinned day-cycle clock and sun, hover-expand panels, lightbox, booking calendar, animated map."),
 "2-festival": ("SALTHOWL Nº9 — music festival", "3:18", "f_0036", "Moving film grain, mouse-reactive letters, pinned colour-shifting scroll section, timetable with clash detection and share link, map with live festival clock, ticket totals."),
 "3-ecommerce": ("KALDER — clothing brand", "5:53", "f_0008", "Load-in wipe, scroll-darkening manifesto, product rail with hover, pinned lookbook with hotspots, product modal that opens from a line, shipping map with drawn routes, live store hours."),
 "4-saas": ("Kestrel — finance SaaS", "7:51", "f_0028", "Coded live dashboard (ticking cash, new rows, typed log), 3D tilt on scroll, step section, month-end close demo, ROI calculator, integrations orbit, pricing toggle, changelog drag."),
 "5-drink": ("HYPERLYTE — 3D sports drink", "9:53", "f_0010", "three.js can with canvas-drawn label, drag to rotate, can travels with scroll, flavour wipe, can opens with particle splash, page recolour per flavour, auto-scrolling reviews."),
 "6-highrise": ("HALDEN — 3D high-rise", "12:35", "f_0008", "Procedural three.js tower and city, scroll camera path, golden hour to dusk lighting, windows light floor by floor, hover and click floors, filters, payment calculator."),
 "7-space": ("KÁRMÁN — 3D space tourism", "14:45", "f_0002", "Procedural rocket, pad and tower, liftoff with smoke, shader Earth with clouds and city lights, stage separation, Moon pass and Earthrise, live altitude and velocity readout."),
}
css = """:root{color-scheme:dark;--bg:#0f172a;--card:#1e293b;--line:#334155;--tx:#e2e8f0;--tx2:#cbd5e1;--mut:#94a3b8;--a:#fb923c;--b:#2dd4bf}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.6 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:1200px;margin:0 auto;padding:40px 16px 80px}h1{font-size:32px;margin:0 0 8px}h2{font-size:24px;margin:0 0 4px}h3{font-size:15px;color:var(--tx2);margin:20px 0 8px}
p,li{color:var(--tx2)}.mut{color:var(--mut);font-size:14px}.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:24px;margin:28px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}figure{margin:0}figure img{width:100%;display:block;border:1px solid var(--line);border-radius:6px}
figcaption{font-size:13px;color:var(--mut);margin-top:6px}figcaption b{color:var(--a)}.code b{color:var(--b)}
.tag{display:inline-block;font-size:12px;border:1px solid var(--line);border-radius:4px;padding:1px 6px;margin:2px;color:var(--tx2)}
.src{color:var(--a)}.cd{color:var(--b)}code{overflow-wrap:anywhere}"""
S = []
tot_files = sum(len(m["files"]) for m in meta.values())
for s, m in meta.items():
    name, ts, fr, anim = INFO[s]
    tags = "".join(f'<span class="tag">{html.escape(n)} · {kb} KB</span>' for n, kb in m["files"])
    S.append(f"""<section class="card" id="{s}"><h2>{html.escape(name)}</h2>
<p class="mut">Video chapter from {ts} · reference frame {fr} · page file <code>sites/{s}/index.html</code> ({m['html_kb']} KB of HTML, CSS and JavaScript, no embedded images) · page height {m['height']:,} px</p>
<div class="grid">
<figure><img src="img/{s}_frame.jpg" alt="Video frame"><figcaption><b>1. Video frame.</b> The original site, as recorded. The presenter's webcam (bottom-left) is blurred.</figcaption></figure>
<figure><img src="img/{s}_with.jpg" alt="Rebuild with images"><figcaption class="code"><b>2. Rebuild, normal.</b> Code plus the generated photos.</figcaption></figure>
<figure><img src="img/{s}_without.jpg" alt="Rebuild with images blocked"><figcaption class="code"><b>3. Rebuild, photos blocked.</b> The browser refused all {len(m['blocked'])} requests to <code>img/</code>. Everything still visible is code.</figcaption></figure>
<figure><img src="img/{s}_without_mid.jpg" alt="Mid-page with images blocked"><figcaption class="code"><b>4. Photos blocked, mid-page</b> (scroll {m['mid']:,} px).</figcaption></figure>
</div>
<h3><span class="src">Generated photos</span>: {len(m['files'])} files, made from text prompts</h3><div>{tags}</div>
<h3><span class="cd">Made in code</span></h3><p>Layout, all text, fonts (Google substitutes), colours, the top banner, and: {html.escape(anim)}</p></section>""")
body = "".join(S)
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark">
<title>Rebuild Evidence</title><style>{css}</style></head><body><main>
<h1>Rebuild evidence: 7 websites from one video</h1>
<p class="mut">Source: <a class="src" href="https://www.youtube.com/watch?v=mPiaap4zEVk">NEW Opus 5.5 is INSANE at Building Websites (Full Showcase)</a> by Brendan Jowett (YouTube, @brendanautomation). In that video, Claude Opus 5.5 builds seven websites. The original sites, their design and their brand names are his work. Rebuilt on 2026-09-24 by Claude Opus 5.5 agents from frames of that video. Not affiliated with Brendan Jowett or Anthropic.</p>
<section class="card"><h2>The claim, stated exactly</h2>
<p>The pages were rebuilt in code. The photos were first cropped from the video, then replaced on 2026-09-25 with new images generated from text prompts.</p>
<ul><li><b class="src">Generated:</b> {tot_files} photo files across the 7 sites. Each was made with Higgsfield (GPT Image 2.5, 4K) from a text description of the scene. No video frame was used as input. Small thumbnails are downscaled from their full images. No file contains page layout, text or buttons.</li>
<li><b class="cd">Written as code:</b> everything else: layout, text, typography, colour, every animation and interaction, and all 3D (three.js geometry built in code, with no downloaded models).</li></ul></section>
<section class="card"><h2>How this page was made</h2>
<ol><li>Each page was opened in Chrome (Playwright, viewport 1600 × 792 CSS px).</li>
<li>Screenshot 2 was taken normally.</li>
<li>For screenshots 3 and 4, the browser refused every request to the site's <code>img/</code> folder. The count of refused requests is under each screenshot.</li>
<li>The video frame is the top half of the side-by-side check made during the build (<code>scratch/verify/</code>).</li></ol>
<p>Script: <code>scripts/evidence.py</code>. Anyone can run it again on the <code>sites/</code> folder.</p></section>
<section class="card"><h2>Tests a skeptic can run without trusting us</h2>
<ol><li><b>Remove the photos.</b> Rename <code>sites/&lt;site&gt;/img</code> and reload. The page still renders and animates; only the photo areas go blank. Screenshots 3 and 4 show the result.</li>
<li><b>Resize the window.</b> Text wraps and the layout reflows. A picture cannot reflow.</li>
<li><b>Search the text.</b> Ctrl+F finds headings and paragraphs, because they are real text.</li>
<li><b>Interact beyond the video.</b> Drag the 3D can to any angle, set the ROI sliders to values the video never shows, pick two clashing festival sets, click any tower floor.</li>
<li><b>Check the live values.</b> Countdowns count from today's date, not the recording date. The SaaS dashboard figures change every second.</li>
<li><b>Read the source.</b> Each page is 50–109 KB of plain HTML, CSS and JavaScript, with no embedded images.</li></ol></section>
<section class="card"><h2>Limits of this evidence</h2>
<ul><li>The crop scripts that linked each photo to its exact source frame were deleted with the working files. The frame numbers survive only in the build reports.</li>
<li>The build order of the code was not recorded.</li>
<li>The rebuilds differ from the originals: substitute fonts, invented text where the video shows none, and no sections that the video never shows.</li>
<li>The video frames included the presenter's webcam. It is blurred here.</li>
<li>The screenshots show the rebuilds before 2026-09-25, when the page text was rewritten and the top banner changed for the public repository.</li></ul></section>
{body}
</main></body></html>"""
open("evidence/index.html", "w", encoding="utf-8").write(page)
print("written", len(page) // 1024, "KB")
