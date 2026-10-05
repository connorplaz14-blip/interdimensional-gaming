#!/usr/bin/env python3
from pathlib import Path
import csv, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
issues=[]
rows=list(csv.DictReader((ROOT/'sources.csv').open(encoding='utf-8')))
for r in rows:
    if r['rights_status'] not in {'GREEN','YELLOW','RED'}:
        issues.append(f"Invalid rights status: {r['asset_id']} {r['rights_status']}")
    if r['rights_status'] != 'GREEN' and r['acquired'].lower() == 'true':
        issues.append(f"Non-GREEN asset marked acquired: {r['asset_id']}")
playlist=json.loads((ROOT/'playlist.json').read_text(encoding='utf-8'))
for item in playlist:
    p=ROOT/'edited'/item['file']
    if not p.exists(): issues.append(f"Playlist file missing: {p}")
print(f"sources={len(rows)} playlist_items={len(playlist)} issues={len(issues)}")
for i in issues: print('ISSUE:', i)
sys.exit(1 if issues else 0)
