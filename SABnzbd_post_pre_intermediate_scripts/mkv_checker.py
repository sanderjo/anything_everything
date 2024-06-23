#!/usr/bin/env python3

# mkv checker, usable as SABnzbd intermediate script

# Hacked together:
# you need mkvmerge and grep, so Linux (and MacOS) only?

import os
import sys

'''
SABnzbd specifies https://sabnzbd.org/wiki/configuration/4.3/scripts/pre-queue-scripts output priority

Priority
-100 = Default
-2 = Paused
-1 = Low
0 = Normal
1 = High
2 = Force
'''


def check_subtitles(mkvfile):
    # ugly way to test if there are subtitles in the mkv
    cmd = f"mkvmerge -J {mkvfile} | grep -i subtitles"
    if os.popen(cmd).readline().find('subtitle') >= 0:
        return True
    else:
        return False


#### MAIN ####

try:
    directory = sys.argv[1]
except:
    print("Error: specify directory")
    sys.exit(-1)

largest_file = max(
    (os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files),
    key=os.path.getsize
)

prio = 0  # default
if largest_file.lower().endswith(".mkv"):
    # yes, mkv
    if check_subtitles(largest_file):
        comment = "MKV, with subs"
        prio = 1
    else:
        comment = "MKV, no subs"
        prio = -1  # or 0 or -2 ...
elif largest_file.lower().endswith(".bin"):
    # my testfile
    comment = "a bin, so maybe the testfile"
    prio = 1
else:
    comment = "Nothing special"

print(prio) # first line is the prio decisions towards SABnzbd
print(largest_file) # the file we considered
print(comment) # comment for humans: why, what

