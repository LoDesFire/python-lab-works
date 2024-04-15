# noinspection PyPropertyDefinition
class FigureColour:
    """Class of figure color"""

    def __init__(self, color="unknown"):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def set_color(self, new_color: str):
        self.__color = new_color if self.__color != new_color else self.__color
