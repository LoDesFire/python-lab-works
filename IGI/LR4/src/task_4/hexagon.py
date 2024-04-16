import math
from math import sqrt, cos, sin
from PIL import Image, ImageDraw, ImageColor, ImageFont

from src.task_4.figure_colour import FigureColour
from src.task_4.geometric_figure import GeometricFigure
from src.task_4.name_mixin import NameMixin


class Hexagon(GeometricFigure, NameMixin):
    """Hexagon figure class"""
    def __init__(self, a: float, color: FigureColour, name: str):
        super().__init__(name)
        self.__a = a
        self.__color = color

    def calculateS(self):
        """Calculating value of the figure area """
        return 3 * sqrt(3) * self.__a ** 2 / 2

    def __str__(self):
        return "Colour: {colour}\nArea: {area}".format(colour=self.__color.color, area=self.calculateS())

    def draw(self):
        """Drawing the figure with Pillow library"""
        points = []
        a = self.__a
        for i in range(0, 6):
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            points.append((500 + a * cos(angle_rad), 500 + a * sin(angle_rad)))
        lowest_point = max(points, key=lambda p: p[1])

        font = ImageFont.truetype("src/task_4/data/font.ttf", 100)
        im = Image.new('RGB', (1000, 1000), ImageColor.getcolor("white", "RGB"))\

        draw = ImageDraw.Draw(im)
        draw.polygon(
            xy=tuple(p for p in points),
            fill=self.__color.color, outline=(0, 0, 0)
        )
        w, h = draw.textsize(self.name, font=font)
        draw.text(
            xy=((1000 - w) / 2, lowest_point[1] + 50),
            text=self.name,
            fill=ImageColor.getcolor("black", "RGB"),
            font=font,
        )

        with open("src/task_4/data/hexagon.png", "wb") as file:
            im.save(file, format="png")

        im.show()
