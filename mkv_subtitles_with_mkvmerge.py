#!/usr/bin/env python3

'''
finds and prints subtitles found in a .mkv file
Needs the binary "mkvmerge", part of mkvtoolnix, available for Linux, MacOS and Windows
'''

import os
import json
import sys

try:
    inputmkvfile = sys.argv[1]
except:
    inputmkvfile = "~/something.mkv"

if not os.path.isfile(inputmkvfile):
    sys.exit("file does not exist " + inputmkvfile)


print("Inspecting", inputmkvfile)

try:
    cmd = "mkvmerge -J " + inputmkvfile
    json_output = os.popen(cmd).read()
except:
    sys.exit("error running mkvmerge")

try:
    mkv_details = json.loads(json_output)
    tracks = mkv_details['tracks']
except:
    sys.exit("error trying to get JSON tracks")

subfounds ={}
for i in tracks:
    if i["type"] == "subtitles":
        sub = i["properties"]["language"]
        subfounds[sub] = 1

#print(subfounds)
if not subfounds:
    print("no subs found")
else:
    for sub in subfounds:
        print(sub, end=" ")
    print(" ")
