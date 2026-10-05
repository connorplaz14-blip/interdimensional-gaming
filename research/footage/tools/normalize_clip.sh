#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 INPUT OUTPUT [--mute]" >&2
  exit 2
fi
IN="$1"; OUT="$2"; MUTE="${3:-}"
VF="scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30"
if [ "$MUTE" = "--mute" ]; then
  ffmpeg -hide_banner -y -i "$IN" -map 0:v:0 -vf "$VF" \
    -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -movflags +faststart -an "$OUT"
else
  ffmpeg -hide_banner -y -i "$IN" -map 0:v:0 -map 0:a? -vf "$VF" \
    -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -movflags +faststart \
    -c:a aac -b:a 160k -ar 48000 "$OUT"
fi
