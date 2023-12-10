#!/usr/bin/env python3

'''
Finding subtitles in .MKV without any external tools
Based on brute-force reverse engineering of an MKV file
'''

import sys

try:
    inputmkvfile = sys.argv[1]
except:
    inputmkvfile = "/home/sander/something.mkv"
    inputmkvfile = "/home/sander/bla-head-c10000.mkv"

subfounds ={}
searchstring = b'TEXT/UTF8'  # this is the subtitle indicator. The subtitle is somewhere before or after that...
startpos = 0

preambleforsublanguage = b"\xb5\x9c\x83" # this is binary string that is right before the language


print(inputmkvfile)

with open(inputmkvfile, 'rb') as f:
    s = f.read(20000) # MKV subtitle info is already in the first part of the MKV, so only read that
    for i in range(100): # max 100 subtitles
        pos = s.find(preambleforsublanguage,startpos)
        if pos < 0:
            # no (more) subtitle info found, so quit the for loop
            break

        #sublanguage = s[preamble_lang+3 : preamble_lang+6]
        sublanguage = s[pos+3 : pos+6]
        print(sublanguage)

        '''
        # OK. Now search before or after that:
        longerstring = s[pos-20:pos+20]

        pos_preamble_lang = longerstring.find(preamble_lang)
        try:
            sublanguage = longerstring[pos_preamble_lang+3:pos_preamble_lang+6].decode('utf-8')
            if all(x.islower() for x in sublanguage):
                # all lowercase letters, so that looks like a language!
                subfounds[sublanguage] = True
        except:
            pass
        '''
        startpos = pos + 10  # skip a bit further


if not subfounds:
    print("no subs found")
else:
    for sub in subfounds:
        print(sub, end=" ")
    print(" ")



