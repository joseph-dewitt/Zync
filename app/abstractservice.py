from abc import ABC, abstractmethod


class AbstractService(ABC):

    # This method is meant to only call directly from the API
    # module, and instantiate group objects
    @abstractmethod
    def get_groups(self):
        pass


class AbstractObject(ABC):

    def __init__(self, body):
        self.data = body

    def __repr__(self):
        return f"{self.__class__.__name__} with id {self['id']} and name {self['name']}"

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
