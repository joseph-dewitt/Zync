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

"""
TODO give these functions named variables
board_id, list_id, card_id, because the API
allows fetching the data in different ways.
Let's use that

They take multiple optional named variables, and 
throw an exception if none are provided 
"""


def get_boards():
    return requests.get(f'{base_url}members/me/boards?filter=open&{auth}').json()


def get_board(board_id=None, list_id=None, card_id=None):
    if board_id:
        return requests.get(f'{base_url}boards/{board_id}?filter=open&{auth}').json()
    if list_id:
        return requests.get(f'{base_url}lists/{list_id}/board?filter=open&{auth}').json()
    if card_id:
        return requests.get(f'{base_url}cards/{card_id}/board?filter=open&{auth}').json()


def get_lists(board_id):
    return requests.get(f'{base_url}boards/{board_id}/lists?filter=open&{auth}').json()


def get_list():
    pass


def get_cards(board_id=None, list_id=None):
    if board_id:
        return requests.get(f'{base_url}boards/{board_id}/cards?{auth}').json()
    if list_id:
        return requests.get(f'{base_url}lists/{list_id}/cards?{auth}').json()
