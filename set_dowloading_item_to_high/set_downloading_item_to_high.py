#!/usr/bin/env python3


'''
SABnzbd pre-queue (aka pre-processing) script to set already Downloading item to prio High.
This avoids that SABnzbd's automatic pushes suchs an item back into the queue

Usage:
Create a SABnzbd script directory
Put this script in that directory. Make it executable. If SAB < 4.3.0: Edit the two indicated lines
As a test, run it directly from that directory (with SABnzbd running)

If that works, in SABnzbd:
Define script directory in http://127.0.0.1:8080/sabnzbd/config/folders/#script_dir
Define pre-queue script: http://127.0.0.1:8080/sabnzbd/config/switches/#pre_script

Done!


Note
Via http://127.0.0.1:8080/sabnzbd/config/switches/#auto_sort ... you can set sorting to anything you want

'''

import os
import sys
import urllib.request
import json


try:
    # this works for SABnzbd 4.3.0 and higher; automagic values FTW
    baseurl = os.environ['SAB_API_URL'] # Often 'http://localhost:8080/sabnzbd/api'
    apikey = os.environ['SAB_API_KEY']
except:
    # edit these two lines if on SABnzbd < 4.3.0, or test run from CLI
    apikey = "f69d7cdb668f4628b4238ff61af0acc8"  # get from http://127.0.0.1:8080/sabnzbd/config/general/#apikey_display
    baseurl = "http://localhost:8080/"
    baseurl = baseurl + "sabnzbd/api"  # do NOT edit


# more global
api_url_queue = f"{baseurl}?output=json&apikey={apikey}&mode=queue" # default: GET queue
loggingtext = ['Logging from script']

def talk_to_sabnzbd(sab_url):
    try:
        # Make the GET request
        response = urllib.request.urlopen(sab_url)
        # Read the response data
        data = response.read().decode('utf-8')
        # Parse JSON
        json_data = json.loads(data)
        return json_data
    except Exception as e:
        print("Error:", e)
        return None

def set_prio_high(nzo_id):
    # Set priority as described on https://sabnzbd.org/wiki/configuration/4.2/api#priority
    # api?mode=queue&name=priority&value=NZO_ID&value2=0 with 1 = High Priority

    # create URL for setting prio of nzo_id to High
    api_url_prioset = f"{api_url_queue}&name=priority&value={nzo_id}&value2=1"

    # do it, 3 times
    result = talk_to_sabnzbd(api_url_prioset)
    return f"result of priosetting: {result}"

    '''
    result = talk_to_sabnzbd(api_url_prioset)
    loggingtext += [f"result of priosetting: {result}"]

    result = talk_to_sabnzbd(api_url_prioset)
    loggingtext += [f"result of priosetting: {result}"]
    '''


# MAIN

# get sab queue
sabnzbd_queue = talk_to_sabnzbd(api_url_queue)
# handle the queue
if not sabnzbd_queue:
    loggingtext += [f'SABnzbd not reachable on {baseurl}']
else:
    all_queue_items = sabnzbd_queue['queue']['slots']
    number_of_items_in_queue = len(all_queue_items)
    loggingtext += [f'Size of queue is {number_of_items_in_queue}']
    for queueitem in all_queue_items:
        if queueitem['status'] == 'Downloading':
            filename = queueitem['filename']
            nzo_id = queueitem['nzo_id']
            percentage = float(queueitem['percentage'])
            priority = queueitem['priority']
            loggingtext += [f"found {filename} as downloading, with priority {priority}"]
            if priority == 'Normal' and percentage > 5.0:
                loggingtext += [f"setting prio of {filename} to High"]
                result = set_prio_high(nzo_id)
                loggingtext += [result]
            break  # done; we found the Downloading item, and handled it

# Just accept this NZB, with these 7 output parameters
print("1")  # Accept the job
print()
print()
print()
print()
print()
print()

# logging that will land in sabnzbd.log (ignored by SABnzbd itself):
for i in loggingtext:
    print("pre-queue script:", i)
sys.exit(0)

