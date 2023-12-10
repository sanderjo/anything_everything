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
search_s_text = b'S_TEXT'  # this is the subtitle indicator. The subtitle language is somewhere before or after that...

# "language", like "slo"
#preamble_lang = b"\xb5\x9c\x83"  # this is binary string that is right before the subtitle language
# TODO take care of the \x83 part!!!
preamble_lang = b"\x22\xb5\x9c" # with "\x83" after that for 3-char language


# "language_ietf", like "sk"
preamble_ietf_lang = b"\x22\xb5\x9d" # and after a \x82 ... ending "2" for ... 2 bytes language. And \x85 for 5 characters like es-ES

startpos = 0

print(inputmkvfile)

with open(inputmkvfile, 'rb') as f:
    s = f.read(20000) # MKV subtitle info is in the first part of the MKV, so only read that

for i in range(100): # max 100 subtitles
    pos = s.find(search_s_text, startpos)
    if pos < 0:
        # no (more) subtitle info found, so quit the for loop
        break

    # OK. Now search around that:

    # language. Always (3) 3-char
    longerstring = s[pos-20:pos+20]
    pos_preamble_lang = longerstring.find(preamble_lang)
    if pos_preamble_lang >=0 :
        try:
            language_length = longerstring[pos_preamble_lang + 3] & 0x0f # only right 4 bits
            #print(language_length)
            sublanguage = longerstring[pos_preamble_lang + 4 : pos_preamble_lang + 4 + language_length].decode('utf-8')
            subfounds[sublanguage] = True
        except:
            pass

    # ietf_language. Often 2-char, but sometimes 5-char like es-ES
    pos_preamble_ietf_lang = longerstring.find(preamble_ietf_lang)
    if pos_preamble_ietf_lang >= 0:
        language_length = longerstring[pos_preamble_ietf_lang + 3] & 0x0f # only right 4 bits
        try:
            sublanguage = longerstring[pos_preamble_ietf_lang + 4: pos_preamble_ietf_lang + 4 + language_length].decode('utf-8')
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



