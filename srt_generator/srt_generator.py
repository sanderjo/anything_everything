'''
1
00:00:32,244 --> 00:00:35,484
Gebaseerd op ware gebeurtenissen

2
00:02:00,519 --> 00:02:06,039
Sinds de dood van Prinses Diana
is Groot-Brittannië in de rouw.

3
00:02:21,225 --> 00:02:23,985
Het klinkt zo mooi, Inger.
-Ja.

4
00:02:24,665 --> 00:02:28,226
Je moet het spelen
op mijn en mama's begrafenis.

'''


from datetime import datetime
from datetime import timedelta

counter = 1 # how many sub-entries
time = datetime.min

while counter<100:
    time = time + timedelta(seconds = 5)
    starttime = time.strftime("%H:%M:%S")
    endtime = (time + timedelta(seconds = 2)).strftime("%H:%M:%S")
    print(counter)
    print(f"{starttime},111  -->  {endtime},999")
    print(f"Nonono nono {counter}")
    print()

    counter += 1



