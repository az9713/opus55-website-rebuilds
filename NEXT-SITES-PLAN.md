# Stage 2 plan: 7 new sites in the style of the 7 rebuilds

Status: **approved, not built.** Final set = Claude's recommended set (section 7). Build starts in a fresh session.
Date: 2026-09-25 (session 5).

## 1. The request

The owner wants 7 new websites. Each new site keeps the STYLE of one of the 7 rebuilt
sites (layout, fonts, animations, tone). The subject and the locale change. Example
from the owner: `1-hotel` is a hotel by the sea; the new site is a hotel with the same
style in a totally different locale.

The owner asked for 3 suggestions for each site, and said: "do not create any new
website yet."

## 2. The 7 source sites

| Site | Brand | Subject and setting |
|---|---|---|
| `1-hotel` | Solenne | Boutique hotel, 34 rooms, Mediterranean coast, warm late-afternoon light |
| `2-festival` | SALTHOWL Nº9 | Raw music festival on a coastal headland (Marrow Head, Gorse Coast) |
| `3-ecommerce` | KALDER | Foul-weather outerwear (AW26), wet pier, orange accent |
| `4-saas` | Kestrel | "The finance desk that runs all night" |
| `5-drink` | HYPERLYTE | Electrolyte drink, 3D can, athletes at night in rain |
| `6-highrise` | HALDEN | 38-storey residential tower on a waterfront (Marlin Quay), 3D model |
| `7-space` | KÁRMÁN | Space tourism capsule, 3D, "Space begins about a hundred kilometres up" |

All new place names will be invented, as in the current sites.

## 3. Claude's A, B, C suggestions

Option A was Claude's first recommendation for each site.

### 1-hotel (Solenne)
- **A.** Mountain ryokan near Kyoto: 20 rooms in a cedar forest, hot-spring baths, snow in winter. The quiet tone of Solenne fits.
- **B.** Desert lodge in the Atacama: adobe suites, stargazing deck. The warm light moves from sea to sand.
- **C.** Fishing-cabin hotel in Lofoten, Norway: red huts on stilts, northern lights. Cold palette, slower tone.

### 2-festival (SALTHOWL)
- **A.** Electronic festival on a salt flat, Bolivia-style. Same raw typography; white ground, night stages.
- **B.** Winter festival on a frozen Nordic lake: ice stages, torch-lit program.
- **C.** Jungle festival among cenotes in the Yucatán: day swims, night program. The brightest palette of the three.

### 3-ecommerce (KALDER)
- **A.** Alpine mountaineering shells on a high glacier. Same product type; wind and snow instead of rain.
- **B.** Desert sun-wear in the Sahara: linen and UV-blocking layers; sand tones instead of grey.
- **C.** Monsoon rainwear in Kerala: tropical rain, green instead of cold grey.

### 4-saas (Kestrel)
A SaaS product has no locale, so each option changes the work. All keep the "runs overnight" idea.
- **A.** Night-shift customs clearance for a container port. Strong image, real overnight need.
- **B.** Overnight hospital pharmacy and supply operations.
- **C.** Contract review for law firms, ready by morning.

### 5-drink (HYPERLYTE)
- **A.** Sparkling matcha energy can, Tokyo night streets. The 3D can stays; label and colours change.
- **B.** Coconut-water recovery drink, Brazilian surf culture.
- **C.** Birch-sap sauna recovery drink, Finnish lake culture.

### 6-highrise (HALDEN)
- **A.** Mass-timber tower beside a Norwegian fjord. The 3D tower needs a new material; the shape can stay similar.
- **B.** Slim tower in a dense Tokyo-style district above a river and rail lines.
- **C.** Cliffside residence between a mountain and the ocean, Cape Town-style. The 3D needs a new shape, so this is the most work.

### 7-space (KÁRMÁN)
- **A.** Stratospheric balloon flights to 30 km at dawn. The capsule can stay much the same.
- **B.** Deep-sea submersible dives to an ocean trench ("The deep begins 200 metres down"). Needs a new 3D vehicle.
- **C.** Lunar surface stays at a Moon hotel. Needs new 3D and a new mission map.

### Numbers given with the suggestions
- Image cost: the first image run used 323.0 Higgsfield credits for 75 images. Balance on 2026-09-25: 325.41.
- The owner then said a paid Higgsfield **API** key is also available in `./.env` and can be used for images. Not yet checked: how the API bills, and whether it uses the same credits.
- 3D effort: 5A, 6A and 7A keep the current 3D models with small changes. 6C, 7B and 7C need new 3D models.

## 4. The owner's choices

`1A 2A 3A 4B 5C 6A 7B`

The owner said: "Do not act on my choices yet."

## 5. The owner's variation requirements

The owner asked whether these choices:

1. maximize the differences, contrasts and variations **from Brendan's 7 sites** in content, and
2. maximize the differences, contrasts and variations **among the 7 new sites themselves**.

If not, Claude was to give its own 7 suggestions.

## 6. Claude's assessment of the owner's choices

**Verdict: no on both requirements.**

### Requirement 1: difference from Brendan's sites (5 of 7 strong)

| Site | Choice | Contrast with the original |
|---|---|---|
| 1 | Kyoto ryokan | Strong: sea to mountain forest |
| 2 | Bolivian salt flat | Strong: green coast to white high desert |
| 3 | Alpine glacier shells | **Weak:** the original already sells technical shells for hostile cold weather. Only rain becomes snow. |
| 4 | Hospital pharmacy | Strong: finance to healthcare |
| 5 | Finnish birch-sap sauna drink | Strong: city at night in rain to lake at rest |
| 6 | Fjord timber tower | **Weak:** the original is a calm tower facing open water; a fjord is also open water |
| 7 | Deep-sea submersible | Strong: up to down |

### Requirement 2: difference among the choices

- **Climate:** 4 of 7 are cold or snowy (1A in snow, 3A, 5C, 6A). 0 of 7 are hot or tropical.
- **Region:** 3 of 7 are in northern or alpine Europe (3A, 5C, 6A); 5C and 6A are both Nordic. None is in Africa, North America, or a dense city.
- **Palette:** 3 of 7 are white-dominated (snow in 1A, salt in 2A, glacier in 3A).

## 7. Claude's recommended set and justification

Recommended: **1A (autumn) · 2C · 3B · 4B · 5C (winter) · 6-new · 7B**

| Site | Recommendation | Climate | Region | Main palette |
|---|---|---|---|---|
| 1 | Kyoto mountain ryokan **in autumn**, not winter | Temperate | Asia | Maple red, amber, moss |
| 2 | Jungle festival among the Yucatán cenotes (2C) | Tropical, humid | North America | Green, turquoise water |
| 3 | Sahara sun-wear: linen and UV-blocking layers (3B) | Hot, dry | Africa | Sand, ochre |
| 4 | Overnight hospital pharmacy and supply operations (4B) | Indoor | Any city | Clinical white, one accent colour |
| 5 | Birch-sap sauna recovery drink, Finland **in winter** (5C) | Cold | Northern Europe | Birch white, lake blue, wood |
| 6 | **New option:** tower with garden terraces in a dense São Paulo-style city, no waterfront | Subtropical, urban | South America | Concrete, planted green |
| 7 | Deep-sea dives to a Pacific trench (7B) | Deep ocean | Pacific | Black, bioluminescent blue |

### Justification for each change
- **3A to 3B:** an alpine shell repeats the original product type and its hostile-weather idea. Sahara sun-wear is the opposite: sun instead of rain, heat instead of cold, sand instead of grey.
- **6A to the new city tower:** a fjord tower repeats the original's waterfront. A dense city with no water removes the main shared feature. It is also the first dense-city site in either set.
- **2A to 2C:** with 3B in the Sahara, a salt flat would give 2 dry-desert sites. The Yucatán jungle adds the only tropical, humid site and the only North American site.
- **1A from snow to autumn, and 5C set in winter:** only one site is then snowy, and the hotel gets a warm palette.
- **4B and 7B kept:** both already contrast strongly with the originals and with the other choices.

### Result of the recommended set
- 7 different climates.
- 6 different regions, plus 1 site with no fixed place (site 4).
- Only 1 cold site (5).
- Only site 7 keeps a link to open water.

### Effort notes (estimates, not checked)
- 7B needs a new 3D vehicle (submersible) in place of the capsule.
- The new site 6 can probably keep the current 3D tower with new materials. The 3D code was not read.
- Images: check the Higgsfield API billing in `./.env` before any generation.

## 8. Final decisions (2026-09-25, session 5)

- **Set:** the recommended set in section 7: 1A (autumn) · 2C · 3B · 4B · 5C (winter) · new city tower · 7B.
- **Location:** same repo, new folder `sites-v2/<N-name>/`. Live on the same GitHub Pages address. README gets a second table.
- **Image budget:** cap at 350 credits for about 75 images (the stage 1 rate was 323.0 credits for 75 images, about 4.3 per image with retries). Check the Higgsfield API billing (`HIGGSFIELD_API_KEY` in `./.env`) first. Stop and ask the owner if the total would pass 350. Subscription balance on 2026-09-25: 325.41 credits.
- **Site 7 submersible:** build the 3D vehicle in Three.js code, as the current 3D sites do. No 3D generation credits.
- **Timing:** handoff, `/clear`, then build in a fresh session.
- **Defaults not asked:** start each new site from a copy of its source `sites/<N-name>/index.html` and keep the style; invent all brand and place names; new images from text prompts only (no stage 1 image as `--image`); commit and push only when the owner asks.

## 9. Open before the build

1. Check the Higgsfield API: how it bills, and the credit balance.
