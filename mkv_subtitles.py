#!/usr/bin/env python3

'''
Finding subtitles in .MKV without any external tools
Based on brute-force reverse engineering of some MKV files with head, hd, grep

Motto: reverse engineering is also engineering!
'''

import sys
import os

try:
    inputmkvfile = sys.argv[1]
except:
    inputmkvfile = "/home/sander/something.mkv"
    inputmkvfile = "/home/sander/bla-head-c10000.mkv"

if not os.path.isfile(inputmkvfile):
    sys.exit("file does not exist " + inputmkvfile)

subfounds ={}
searchstring = b'S_TEXT'  # this is the subtitle indicator. The subtitle language is somewhere before or after that...

# "language", like "slo"
preambleforsublanguage = b"\xb5\x9c\x83"  # this is binary string that is right before the subtitle language
# TODO take care of the \x83 part!!!
# preamble_lang = b"\x22\xb5\x9c" # with "\x83" after that for 3-char language

# "language_ietf", like "sk"
preamble2 =b"\x22\xb5\x9d" # and after a \x82 ... ending "2" for ... 2 bytes language. And \x85 for 5 characters like es-ES

startpos = 0

print(inputmkvfile)

with open(inputmkvfile, 'rb') as f:
    s = f.read(20000) # MKV subtitle info is in the first part of the MKV, so only read that

for i in range(100): # max 100 subtitles
    pos = s.find(searchstring,startpos)
    if pos < 0:
        # no (more) subtitle info found, so quit the for loop
        break

    # OK. Now search before and after that:
    longerstring = s[pos-20:pos+20]
    pospreambleforsublanguage = longerstring.find(preambleforsublanguage)
    if pospreambleforsublanguage >=0 :
        try:
            sublanguage = longerstring[pospreambleforsublanguage+3:pospreambleforsublanguage+6].decode('utf-8')
            if all(x.islower() for x in sublanguage):
                # all lowercase letters, so that certainly looks like a subtitle language!
                subfounds[sublanguage] = True
        except:
            pass
    else:
        # can we find a 2 byte language then ... ?
        twobytepos = longerstring.find(preamble2)
        if twobytepos >= 0:
            length = longerstring[twobytepos+3] - 8*16
            print(length)
            try:
                sublanguage = longerstring[twobytepos+4 : twobytepos+4+length].decode('utf-8')
                print(sublanguage)
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



