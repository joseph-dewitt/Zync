from app.helpers import normalize_list
from .trello import *
from .trellotransforms import *
from app.abstractservice import AbstractService, Group, Unit, Element
# TODO all of these functions need exception handling


class TrelloService(AbstractService):

    @normalize_list(map_board_to_group)
    def get_groups(self):
        return get_boards()

    @normalize_list(map_list_to_unit)
    def get_units(self, board_id):
        return get_lists(board_id)

    @normalize_list(map_card_to_element)
    def get_elements(self, unit):
        return get_cards()


class Board(Group):

    @property
    def units(self):
        return get_lists(board_id=self['id'])

    @property
    def elements(self):
        return get_cards(board_id=self['id'])


class List(Unit):

    @property
    def group(self):
        return get_board()

    @property
    def elements(self):
        return get_cards(list_id=self['id'])


class Card(Element):

    @property
    def group(self):
        return get_board(card_id=self['id'])

    @property
    def unit(self):
        return get_list(card_id=self['id'])
