import json
import jsonpath
import requests


base_url = "https://api.publicapis.org/entries"
response = requests.get(base_url)


# Assert that endpoint is returning the right status code
assert (response.status_code == 200)
entries_all = response.json()

#create for loop to select specific entries and their attributes
for entry in entries_all['entries']:
    if entry['Category'] == "Security":
        assert entry['Category'] == "Security"
        #print(entry['API'], entry['Link'])
        print(entry['API']+"  "+entry['Link'])



