# Saved source files

This is the code shelf, not the game-download page. **Want to play? Use the [game guide](README.md) first.**

We keep **ten source archives**: saved copies of selected creator projects. They're useful if you want to see how a mod works or build it yourself. The three October 6 additions are OWCraft, Killcraft and Minecraft Ring.

[← Main page](../README.md) · [Beginner guide](../START-HERE.md) · [Creator credits](../CREDITS.md)

## What's saved here?

| Project | Original creator | Saved source | Licence |
| --- | --- | --- | --- |
| [SkyCraft](https://github.com/chasmlol/SkyCraft) | chasmlol | [Archive](source-archives/skycraft-bfcaf178.tar.gz) | MIT |
| [2010 Rust Rewrite Mashup](https://github.com/chasmlol/2010-rust-rewrite-mashup) | chasmlol; IW4L by vladtrc | [Archive](source-archives/mw2-skate-minecraft-f608f85e.tar.gz) | Apache-2.0; fonts keep their own licences |
| [Universal Modder](https://github.com/rehan-remade/universal-modder) | Rehan Sheikh and contributors | [Archive](source-archives/universal-modder-0f5dcdfd.tar.gz) | MIT |
| [LibertyCraft](https://github.com/mrborghini/libertycraft) | mrborghini and contributors | [Archive](source-archives/libertycraft-aa216d72.tar.gz) | MIT; third-party notices retained |
| [Minecraft crossover bridge](https://github.com/justbustin/minecraft-crossover-bridge) | justbustin | [Archive](source-archives/minecraft-crossover-bridge-d1723873.tar.gz) | MIT; MinHook notices retained |
| [NucleDoom](https://github.com/Patbox/nucledoom) | Patbox and contributors | [Archive](source-archives/doom-minecraft-717b9df9.tar.gz) | LGPL-3.0 for code/non-WAD assets |
| [DoomMaps](https://github.com/ssquadteam/DoomMaps) | ssquadteam | [Archive](source-archives/doom-hytale-2e782ad4.tar.gz) | GPL-3.0 |
| [OWCraft](https://github.com/Yaekai/OWCraft) | Yaekai; based on SkyCraft | [Archive](source-archives/owcraft-cd5f0613.tar.gz) | MIT; SkyCraft notices retained |
| [Killcraft](https://github.com/goonsn/Killcraft) | goonsn / Killcraft authors; based on SkyCraft | [Archive](source-archives/killcraft-ce05bae4.tar.gz) | MIT, including SkyCraft credit |
| [Minecraft Ring](https://github.com/siddoff/Minecraft-Ring) | siddoff; upstream bridge by justbustin | [Archive](source-archives/minecraft-ring-ffb31b55.tar.gz) | MIT; upstream and MinHook notices retained |

Other games in the guide link to the creator's original files. We haven't mirrored every project.

## How to open an archive

Click **Archive**, then download the file from its GitHub file page. A .tar.gz file is a compressed folder; extract it with an archive tool. Inside, look for the project's README and licence files.

For developers, the equivalent command is:

```bash
tar -xzf skycraft-bfcaf178.tar.gz
```

Extracting files doesn't install a mod. Follow that project's own build instructions if you want to compile it. Dependencies or submodules may need separate downloads.

## Which version is it?

The letters and numbers in each filename identify the saved source version. These copies stay fixed; they aren't automatically updated.

[Full archive records](snapshots.json) include checksums (file fingerprints), sizes and licence-file locations. [Earlier collection details](additional-snapshots.json) document the four additions from the previous pass. [New project checks](../research/verified-projects-2026-10-06.json) record the latest documentation review.

NucleDoom's three WAD files were omitted from our copy. Their paths are recorded in the earlier collection details. Use the creator's instructions to obtain the required game content.

We checked the archives and their notices, but **didn't execute or build the upstream code**. Original licences and notices remain inside the archives; there isn't one blanket licence covering every game here.
