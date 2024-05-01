#!/usr/bin/env python3

import sys

try:
    # Parse the input variables for SABnzbd version >= 4.2.0
    (scriptname, nzbname, postprocflags, category, script, prio, downloadsize, grouplist) = sys.argv
except Exception:
    sys.exit(1)  # a non-zero exit status causes SABnzbd to ignore the output of this script

prio = -100  # Default
if int(downloadsize) < 50_000_000:
    prio = 2

print("1")  # Accept the job
print()
print()
print()
print()
print(prio)
print()

# 0 means OK
sys.exit(0)

