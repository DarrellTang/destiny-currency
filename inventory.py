import requests
import re
import json

exp_urlpost = r'urlPost:\'(https://.*?)\''
exp_ppft = r'<input type="hidden" name="PPFT" id=".*" value="(.*?)"/>'

url_signin = 'https://www.bungie.net/en/User/SignIn/Xuid?bru=%252f'

urlprefix = 'https://www.bungie.net/Platform/Destiny/'
apikey = 'cb4710bcf9a74616ac611aa1034f57a3'
liveuser = input("Microsoft Account Email: ")
livepass = input("Password: ")

s = requests.Session()
s2 = requests.Session()
r = s.get(url_signin)
url_post = re.findall(exp_urlpost, r.content.decode())[0]
ppft = re.findall(exp_ppft, r.content.decode())[0]
payload = { 'login': liveuser, 'passwd': livepass, 'PPFT': ppft }
r = s.post(url_post, data = payload)

apiheaders = {'X-API-Key': apikey, 'x-csrf': s.cookies.get_dict()['bungled']}
r = s.get(urlprefix + 'SearchDestinyPlayer/1/endymioncalcite/',headers=apiheaders)

membershipId = r.json()['Response'][0]['membershipId']
r = s.get(urlprefix + '/1/Account/' + membershipId + '/Summary/',headers=apiheaders)
for inventoryItem in r.json()['Response']['data']['inventory']['items']:
    if "primaryStat" not in inventoryItem:
        itemHash = str(inventoryItem['itemHash'])
        quantity = str(inventoryItem['quantity'])
        itemManifest = s2.get(urlprefix + 'Manifest/6/' + itemHash,headers=apiheaders)
        print(itemManifest.json()['Response']['data']['inventoryItem']['itemName'])
        print('Quantity: ' + quantity + "\n")