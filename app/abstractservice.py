from abc import ABC, abstractmethod


class AbstractService(ABC):

    @abstractmethod
    def get_groups(self):
        pass

    @abstractmethod
    def get_units(self, group):
        pass

    @abstractmethod
    def get_elements(self, unit):
        pass


class AbstractObject(ABC):

    def __init__(self, body):
        self.data = body

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]


class Group(AbstractObject):

    @abstractmethod
    def units(self):
        pass


class Unit(AbstractObject):

    @abstractmethod
    def group(self):
        pass

    @abstractmethod
    def elements(self):
        pass


class Element(AbstractObject):

    @abstractmethod
    def group(self):
        pass

    @abstractmethod
    def unit(self):
        pass
