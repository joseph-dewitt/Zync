from .trello import *
from .trellotransforms import *
from app.abstractservice import AbstractService, Group, Unit, Element
# TODO all of these functions need exception handling


class TrelloService(AbstractService):

    @staticmethod
    def get_groups():
        return [Board(body) for body in get_boards()]


class Board(Group):

    @property
    def units(self):
        return [List(body) for body in get_lists(board_id=self['id'])]

    @property
    def elements(self):
        return [Card(body) for body in get_cards(board_id=self['id'])]


class List(Unit):

    @property
    def group(self):
        return Board(get_board())

    @property
    def elements(self):
        return [Card(body) for body in get_cards(list_id=self['id'])]


class Card(Element):

    @property
    def group(self):
        return Board(get_board(card_id=self['id']))

    @property
    def unit(self):
        return List(get_list(card_id=self['id']))
