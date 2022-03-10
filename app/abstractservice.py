from abc import ABC, abstractmethod


class AbstractService(ABC):
    """Provide an interface for all service modules."""
    # This method is meant to only call directly from the API
    # module, and instantiate group objects
    @abstractmethod
    def get_groups(self):
        """Return the highest level object from the service."""
        pass

"""
This is the class for OBJECTS that arrive in from the services
Therefore the mapping to normal form must be declared as a class variable
Rather than an instance variable
"""
class AbstractObject(ABC):
    """
    An intermediary for the normal form of all data returned by services.
    
    The abstract object's chief feature is access to values via bracket notation.
    """

    def __init__(self, data):
        """
        The constructor for the AbstractObject class.

        Parameter:
            _data (dict): The block of data representing the object.
        """
        self._data = data

    def __repr__(self):
        """Provide a brief statement with the object's id and name."""
        return f"{self.__class__.__name__} with id {self['id']} and name {self.get('name')}"

    def __setitem__(self, key, value):
        """Assign the key/value pair to the object's data member variable."""
        self._data[key] = value

    def __getitem__(self, key):
        """Return the value assigned to the key in the data member variable."""
        return self._data[key]

    """
    TODO the user should declare the mapping to the normal form here
    as a CLASS variable
    """

    """
    TODO the user then needs an opportunity to declare relationships to other objects
    This may be handled by the normal form instead
    """

"""
I'm going to squash these three classes into one
This one object will be able to have a FIELD that relates to
itself (another object of type AbstractObject)
"""
class Group(AbstractObject):
    """
    The highest level object that a service delivers.
    
    The Group object represents an object in a service that does not belong
    to any higher element, except possibly a user. It can have many units.
    """

    @abstractmethod
    def units(self):
        """Return all of the Units owned by this group."""
        pass


class Unit(AbstractObject):
    """
    The middle level object that a service delivers.

    The Unit object always belongs to a Group. It can have many Elements.
    """

    @abstractmethod
    def group(self):
        """Return the Group this Unit belongs to."""
        pass

    @abstractmethod
    def elements(self):
        """Return all of the Elements owned by this group."""
        pass


class Element(AbstractObject):
    """The lowest level object that a service delivers.

    The Element object always belongs to a Unit. It does not have
    any AbstractObjects below it.
    """

    @abstractmethod
    def group(self):
        """Return the Group this Element's Unit belongs to."""
        pass

    @abstractmethod
    def unit(self):
        """Return the Unit this Element belongs to."""
        pass
