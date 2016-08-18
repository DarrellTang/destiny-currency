import requests
import re
import json

apikey = 'cb4710bcf9a74616ac611aa1034f57a3'
HEADERS = {"X-API-Key":'cb4710bcf9a74616ac611aa1034f57a3'}
urlprefix = 'https://www.bungie.net/Platform/Destiny/'

s = requests.Session()
itemHash = input("Please enter item hash: ")
printJson = input("Would you like JSON output? (y/n): ")
itemManifest = s.get(urlprefix + 'Manifest/6/' + itemHash,headers=HEADERS)
if printJson == "y":
	print(json.dumps(itemManifest.json(),indent=4))
else:
	print(itemManifest.json()['Response']['data']['inventoryItem']['itemName'])
	
