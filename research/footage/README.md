# INTER DIMENSIONAL GAMING — Footage Acquisition Package

**Acquisition snapshot:** 4 October 2026

## Result

The task reached outcome **B**, not outcome A.

- **GREEN gameplay actually acquired:** **0:00**
- **YELLOW/RED creator footage ripped or redistributed:** **0 files**
- **Publishable master generated:** **No** — generating one would have required unlicensed social/video footage or pretending a code licence grants video rights.
- **Verified self-capture plan:** **31:00 across 10 combinations**
- **Candidate creator footage:** catalogued in `sources.csv` / `sources.json`
- **Permission queue:** `permission-needed.md`
- **Capture queue:** `capture-plan.md` and `metadata/capture-targets.*`

## Why the master is intentionally absent

The strongest viral footage does not carry a verified Creative Commons/general redistribution licence. Open-source licences on SkyCraft, Universal Modder, the 2010 Mashup, LibertyCraft and other codebases govern the covered repository work; they do not automatically transfer copyright in someone else's gameplay recording.

The cleanest legal route is therefore fresh project-owned capture. This runtime does not have the required licensed commercial games installed and cannot launch the Windows/Apple-Silicon game setups. It also cannot fetch GitHub binary release/media bytes through its text-only repository connector. No shady video-ripping service or platform bypass was used.

## What is ready

### Reproducible capture anchors

- **Minecraft × Skyrim — SkyCraft v0.1.2 (MIT)**
- **Minecraft × GTA V — Universal Modder passthrough (MIT)**
- **Minecraft × MW2 / Skate 3 × MW2 / triple mashup — 2010 Rust Rewrite Mashup v0.4.0 (Apache-2.0)**
- **Minecraft × GTA IV — LibertyCraft (MIT)**
- **Minecraft × Elden Ring + Minecraft × Monster Hunter: World — minecraft-crossover-bridge (MIT)**
- **Doom × Minecraft — NucleDoom (LGPL-3.0 for code/non-WAD assets; WAD licences separate)**
- **Doom × Hytale — DoomMaps (GPL-3.0)**

The capture plan is deliberately balanced so one game does not consume the whole channel.

### Strong permission-dependent footage

Tobyn Jacobs (Minecraft × Elden Ring), Swirly (Minecraft × Mario 64), Luckey Faraday (BO2 × Minecraft), InfernoPlus (Morrowind × Elden Ring), luki-1/ArkWeb (Spider-Man × Arkham Knight), Rehan Sheikh's creator demo, and chasm's existing social/YouTube demos.

### Reference-only leads

Tarkov × Skyrim, COD × Mario 64 and COD Zombies × Mario Kart stay out of the distributed package until provenance/rights are resolved.

## Folder layout

```text
interdimensional-footage/
├── raw/
│   ├── minecraft-skyrim/
│   ├── minecraft-gta5/
│   ├── minecraft-elden-ring/
│   ├── minecraft-mw2/
│   ├── skate-mw2/
│   ├── minecraft-skate-mw2/
│   ├── minecraft-mario64/
│   ├── bo2-minecraft/
│   ├── morrowind-elden-ring/
│   ├── tarkov-skyrim/
│   ├── minecraft-gta4/
│   ├── minecraft-monster-hunter-world/
│   ├── doom-minecraft/
│   ├── doom-hytale/
│   ├── spiderman-arkham-knight/
│   └── other/
├── edited/
├── web/
├── metadata/
├── tools/
├── sources.csv
├── sources.json
├── playlist.json
├── permission-needed.md
├── capture-plan.md
└── README.md
```

## Editing workflow

1. Put untouched project-owned or creator-approved footage in the matching `/raw/` folder.
2. Record permission/provenance in `sources.csv` before editing.
3. Normalize approved clips with `tools/normalize_clip.sh`.
4. Place normalized approved clips in `/edited/`.
5. Run `tools/build_montage.py` to create the master and muted autoplay copy.
6. Never add a YELLOW or RED asset to the publishable playlist just because it is publicly downloadable.

## Encoding target

Normalized clips: H.264 MP4, 1920×1080, 30 fps output for broad browser compatibility, square pixels, AAC 160 kb/s when audio is retained, `+faststart`. The web master is generated muted. No CRT scanlines/static are baked into footage.

## New discoveries added during this acquisition pass

- **LibertyCraft — Minecraft × GTA IV**, public MIT project, created 3 Oct 2026.
- **minecraft-crossover-bridge — Minecraft × Elden Ring / Monster Hunter: World**, public MIT project for Apple Silicon + CrossOver.
- **ArkWeb — Spider-Man Remastered × Batman: Arkham Knight**, credible passthrough/cross-simulation project, but its repository currently has no detected licence, so creator permission is required before redistribution.
- **DoomMaps — Doom × Hytale**, GPL-3.0 source project using Doom shareware workflow.

## Important rights rule

`code_rights` and `media_rights` must stay separate. A MIT/Apache/GPL source repository is **not** a blanket licence for a YouTube/X/TikTok gameplay recording or for unrelated publisher-owned game assets.
