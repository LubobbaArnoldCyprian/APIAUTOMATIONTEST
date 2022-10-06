import requests

# Variables
base_url = "https://api.publicapis.org/entries"
category = 'Category'
category_item_security = "Security"
all_entries = 'entries'
ok_status_code = 200
entry_item_api = 'API'
entry_item_link = 'Link'

response = requests.get(base_url)
# Assert that endpoint is returning the right status code
assert (response.status_code == ok_status_code)

entries_all = response.json()
for entry in entries_all[all_entries]:
    if entry[category] == category_item_security:
        assert entry[category] == category_item_security
        print(entry[entry_item_api], entry[entry_item_link])
