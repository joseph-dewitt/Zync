import os
import pprint as pp
import requests

API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')

base_url = 'https://api.trello.com/1/'
auth = f'key={API_KEY}&token={TOKEN}'
result = requests.get(f'{base_url}boards/560bf4298b3dda300c18d09c?fields=name,url&{auth}')

boards = requests.get(f'{base_url}/members/me/boards?fields=name,id&{auth}')
print(result.json())
pp.pprint(boards.json())
info = []
for board in boards.json():
    stuff = requests.get(f'{base_url}/boards/{board.get("id")}/cards?{auth}').json()
    info.append(stuff)

pp.pprint(info)