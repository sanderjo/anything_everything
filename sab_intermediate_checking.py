import requests
import os
import urllib
import json
api_url_queue = "http://localhost:8080/myjson"
api_url_queue = 'http://localhost:8080/sabnzbd/api?output=json&apikey=f69d7cdb668f4628b4238ff61af0acc8&mode=queue'

def get_biggest_file(directory):
    if os.path.isdir(directory):
        largest_file = max(
           (os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files),
           key=os.path.getsize
        )
        return(largest_file)
    else:
        return None

def get_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
def get_ext(file):
    # get extension, in lower case. Safe for None
    #extension = os.path.split(str(file))[1].lower()
    if file:
        extension = os.path.splitext(file)[-1]
    else:
        extension = None
    print("get_ext extension", extension)
    return extension

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
    print(api_url_prioset)

    # do it, 3 times
    result = talk_to_sabnzbd(api_url_prioset)
    return f"result of priosetting: {result}"

def main():
    incomplete = "/home/sander/Downloads/incomplete/" # todo: get from ini
    complete = "/home/sander/Downloads/complete/" # todo: get from ini
    # directunpack =  # todo: get from ini. Bail out if not set


    json_data = get_json_data(api_url_queue)

    if json_data is not None:
        # Process the JSON data as a dictionary
        my_dict = json_data
        print("Retrieved JSON data:")
        print(my_dict)
        print(my_dict['queue']['slots'])
        for queueitem in my_dict['queue']['slots']:
            #print("SJ:", item, item['filename'], item['mb'], item['priority'])
            print("Inspecting", queueitem)


            filename = queueitem['filename']
            nzo_id = queueitem['nzo_id']
            percentage = float(queueitem['percentage'])
            priority = queueitem['priority']
            status = queueitem['status']
            mbdone = float(queueitem['mb']) - float(queueitem['mbleft'])

            if status == 'Downloading':
                print("Downloading", filename)

                ...
                print(priority)
                print(filename)
                print(percentage)
                if priority != "Normal":
                    break # done; already other prio set: High or Low
                myincomplete = incomplete + filename
                myunpack = complete + "/_UNPACK_" + filename
                print(myincomplete)
                print(myunpack)
                myincomplete_biggest = get_biggest_file(myincomplete)
                myunpack_biggest = get_biggest_file(myunpack)
                print("biggest file in myincomplete", myincomplete_biggest)
                print("biggest file in myunpack", myunpack_biggest)

                for file in (myincomplete_biggest, myunpack_biggest):
                    print("file", file)
                    print("ext", get_ext(file))
                    if get_ext(file) == '.mkv':
                        print("Ja, mkv")
                        # todo: checks subs
                        # set_prio_high
                        result = set_prio_high(nzo_id)
                        print(result)

                break # there should only be one Downloading, right
            if status == 'Paused':
                # this queue item is paused, so continue to next item
                print("Not downloading", filename)
                continue # next item in for loop


if __name__ == "__main__":
    main()

