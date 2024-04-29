#!/usr/bin/env python3

'''
SABnzbd pre-queue (aka pre-processing script)
Checks if there is a download with Normal priority & already downloading.
If so, sets it to High priority, so that it will keep downloading (=goal), no matter the automatic sorting


Usage:
Create a script directory
Put this script in that directory. Make it executable. Edit the two lines
As a test, run it directly from that directory

In SABnzbd:
Define script directory in http://127.0.0.1:8080/sabnzbd/config/folders/#script_dir
Define pre-queue script: http://127.0.0.1:8080/sabnzbd/config/switches/#pre_script

Done!


Note
http://127.0.0.1:8080/sabnzbd/config/switches/#auto_sort ... you can set sorting to anything you want

'''

# edit these two lines
baseurl = "http://localhost:8080/"
apikey = "f69d7cdb668f4628b4238ff61af0acc8" # get from http://127.0.0.1:8080/sabnzbd/config/general/#apikey_display
# do not edit below

import sys
import urllib.request
import json


api_url_queue = f"{baseurl}/sabnzbd/api?output=json&apikey={apikey}&mode=queue"

def talk_to_sabnzbd(sab_url):
    try:
        # Make the GET request
        response = urllib.request.urlopen(api_url_queue)
        # Read the response data
        data = response.read().decode('utf-8')
        # Parse JSON
        json_data = json.loads(data)
        return json_data
    except Exception as e:
        print("Error:", e)
        return None

# MAIN
debug = False

if __name__ == "__main__":
    # get sab queue
    sabnzbd_queue = talk_to_sabnzbd(api_url_queue)
    if sabnzbd_queue:
        if debug:
                print(json.dumps(sabnzbd_queue, indent=4))
        all_queue_items = sabnzbd_queue['queue']['slots']
        for queueitem in all_queue_items:
            if debug:
                print(queueitem)
            if queueitem['status'] == 'Downloading':
                filename = queueitem['filename']
                nzo_id = queueitem['nzo_id']
                percentage = float(queueitem['percentage'])
                priority = queueitem['priority']
                if debug:
                    print(f"found {filename} as downloading")
                if priority == 'Normal' and percentage > 5.0:
                    # Set priority as described https://sabnzbd.org/wiki/configuration/4.2/api#priority
                    # api?mode=queue&name=priority&value=NZO_ID&value2=0 with 1 = High Priority
                    if debug:
                        print(f"setting prio of {filename} to High")
                    api_url_prioset = f"{api_url_queue}&name=priority&value={nzo_id}&value2=1"

                break # done; we found the Downloading item
    for i in range(7):
        print()
    sys.exit(0)