import requests

def get_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    api_url = "http://localhost:8080/myjson"
    api_url = 'http://localhost:8080/sabnzbd/api?output=json&apikey=f69d7cdb668f4628b4238ff61af0acc8&mode=queue'
    json_data = get_json_data(api_url)

    if json_data is not None:
        # Process the JSON data as a dictionary
        my_dict = json_data
        print("Retrieved JSON data:")
        print(my_dict)
        print(my_dict['queue']['slots'])
        for item in my_dict['queue']['slots']:
            #print("SJ:", item, item['filename'], item['mb'], item['priority'])
            print("XXX", item)
            print(item['status'])
            if item['status'] == 'Paused':
                # this queue item is paused, so continue to next item
                continue
            if item['status'] == 'Downloading':
                pass
            print(item['priority'])
            print(item['filename'])
            print(item['percentage'])


if __name__ == "__main__":
    main()

