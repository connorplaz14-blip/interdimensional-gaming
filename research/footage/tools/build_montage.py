#!/usr/bin/env python3
from pathlib import Path
import subprocess, json, sys, shlex

ROOT = Path(__file__).resolve().parents[1]
EDITED = ROOT / "edited"
WEB = ROOT / "web"
MASTER = ROOT / "interdimensional-gaming-master.mp4"
MUTED = ROOT / "interdimensional-gaming-web-muted.mp4"
PLAYLIST = ROOT / "playlist.json"

clips = sorted(p for p in EDITED.glob("*.mp4") if p.is_file())
if not clips:
    print("No approved normalized MP4 clips found in edited/. Master not generated.", file=sys.stderr)
    sys.exit(3)

WEB.mkdir(exist_ok=True)
concat = ROOT / "metadata" / "concat.txt"
concat.write_text("".join(f"file '{p.as_posix().replace(chr(39), chr(39)+chr(92)+chr(39)+chr(39))}'\n" for p in clips), encoding="utf-8")

# Clips are expected to have been normalized to matching H.264/AAC parameters.
subprocess.run(["ffmpeg","-hide_banner","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy","-movflags","+faststart",str(MASTER)], check=True)
subprocess.run(["ffmpeg","-hide_banner","-y","-i",str(MASTER),"-map","0:v:0","-c:v","copy","-an","-movflags","+faststart",str(MUTED)], check=True)

manifest=[]
for p in clips:
    probe=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(p)],capture_output=True,text=True,check=True)
    manifest.append({"file":p.name,"title":p.stem.replace('-', ' ').upper(),"project":"","creator":"","duration":round(float(probe.stdout.strip()),3)})
PLAYLIST.write_text(json.dumps(manifest,indent=2),encoding="utf-8")
print(f"Built {MASTER.name}, {MUTED.name}, and playlist.json from {len(clips)} approved clips.")
