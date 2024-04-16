# noinspection PyPropertyDefinition
class NameMixin:
    """Mixin for the naming"""
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_setter(self, val):
        self.__name = val