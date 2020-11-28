import requests
import json
import boto3

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': 'c444ed982a7692768e7389d1e6e845aba1f19a428c36e9e2c33d3586de027bb6'
}
request = requests.get('https://api.trakt.tv/movies', headers=headers)
r = request.text

rlist = requests.get('https://api.trakt.tv/lists/trending', headers=headers)
iddList = rlist.json()[2]['list']['ids']['trakt']
url = 'https://api.trakt.tv/lists/{id}/items/movies'.format(id=iddList)

ritem = requests.get(url, headers=headers)
##jsonR = json.loads(request.text)
itemList = json.loads(ritem.text)

##print(len(jsonR))

credentials = {
    'aws_access_key_id': 'PO/EFNAW6CYkPaVurtU1FKzQl0vCA+qWE0ZrA66n',
    'aws_secret_access_key': 'PO/EFNAW6CYkPaVurtU1FKzQl0vCA+qWE0ZrA66n'
}

with open('movies.json', 'w') as file:
    json.dump(itemList, file)

s3 = boto3.client('s3')
s3.put_object(Body='movies.json', Bucket='proyecto.final.pruebas', Key="prueba/endopoint/items/movies.json")
