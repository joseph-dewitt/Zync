import os
import requests

TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')

base_url = 'https://api.trello.com/1/'
auth = f'key={TRELLO_API_KEY}&token={TRELLO_TOKEN}'
# result = requests.get(f'{base_url}boards/560bf4298b3dda300c18d09c?fields=name,url&{auth}')

# boards = requests.get(f'{base_url}/members/me/boards?fields=name,id&{auth}')
# print(result.json())
# pp.pprint(boards.json())
# info = []
# for board in boards.json():
#     stuff = requests.get(f'{base_url}/boards/{board.get("id")}/cards?{auth}').json()
#     info.append(stuff)
#
# pp.pprint(info)
# TODO all of these functions need exception handling


def get_boards():
    return requests.get(f'{base_url}members/me/boards?filter=open&{auth}').json()


def get_lists(board_id):
    return requests.get(f'{base_url}boards/{board_id}/lists?filter=open&{auth}').json()


def get_cards(list_id):
    return requests.get(f'{base_url}lists/{list_id}/cards?{auth}').json()
