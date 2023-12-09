#!/usr/bin/env python3

'''
Finding subtitles in .MKV without any external tools
Based on brute-force reverse engineering of an MKV file
'''

import sys

try:
    inputmkvfile = sys.argv[1]
except:
    inputmkvfile = "~/something.mkv"
    #inputmkvfile = "/home/sander/bla-head-c10000.mkv"

subfounds ={}
searchstring = b'TEXT/UTF8"\xb5\x9c\x83'  # this is the start of a subtitle indicator
startpos = 0

with open(inputmkvfile, 'rb') as f:
    s = f.read(20000) # MKV subtitle info is already in the first part of the MKV, so only read that
    for i in range(100):
        pos = s.find(searchstring,startpos) #NB: might be -1 !!!
        if pos < 0:
            # no (more) subtitle info found, so quit the for loop
            break
        #print(pos, s[pos:pos+20])
        try:
            sublanguage = s[pos+len(searchstring) : pos+len(searchstring)+3].decode('utf-8')
            subfounds[sublanguage] = True
        except:
            pass
        startpos = pos + 10  # skip a bit further

if not subfounds:
    print("no subs found")
else:
    for sub in subfounds:
        print(sub, end=" ")
    print(" ")




