import math
from math import sqrt, cos, sin
from PIL import Image, ImageDraw, ImageColor, ImageFont

from task_4.figure_colour import FigureColour
from task_4.geometric_figure import GeometricFigure


class Hexagon(GeometricFigure):
    def __init__(self, a: float, color: FigureColour):
        self.__a = a
        self.__color = color

    def calculateS(self):
        return 3 * sqrt(3) * self.__a ** 2 / 2

    def __str__(self):
        return "Colour: {colour}\nArea: {area}".format(colour=self.__color.color, area=self.calculateS())

    def draw(self, text):
        points = []
        a = self.__a
        for i in range(0, 6):
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            points.append((500 + a * cos(angle_rad), 500 + a * sin(angle_rad)))
        lowest_point = max(points, key=lambda p: p[1])

        font = ImageFont.truetype("task_4/data/font.ttf", 100)
        im = Image.new('RGB', (1000, 1000), ImageColor.getcolor("white", "RGB"))\

        draw = ImageDraw.Draw(im)
        draw.polygon(
            xy=tuple(p for p in points),
            fill=self.__color.color, outline=(0, 0, 0)
        )
        w, h = draw.textsize(text, font=font)
        draw.text(
            xy=((1000 - w) / 2, lowest_point[1] + 50),
            text=text,
            fill=ImageColor.getcolor("black", "RGB"),
            font=font,
        )

        with open("task_4/data/hexagon.png", "wb") as file:
            im.save(file, format="png")
