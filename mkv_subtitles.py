#!/usr/bin/env python3

import os
import json


cmd = "mkvmerge -J ~/something.mkv"
json_output = os.popen(cmd).read()
mkv_details = json.loads(json_output)

tracks = mkv_details['tracks']

for i in tracks:
    if i["type"] == "subtitles":
        print(i["properties"]["language"])
