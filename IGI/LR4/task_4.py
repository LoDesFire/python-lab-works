from PIL import ImageColor

from task_4 import Hexagon, FigureColour, Input


def task_4():
    a = Input.input_with_checking(
        float,
        "Input a size of hexagon: ",
        lambda num: 10 <= num <= 400
    )
    color_str = Input.input_with_checking(
        str,
        "Input colour string: ",
        lambda s: type(ImageColor.getcolor(s, "RGB")) == tuple
    )
    image_sign = input("Image sign: ")

    hexagon = Hexagon(a, FigureColour(color_str))
    hexagon.draw(image_sign)
    print(f"\n{hexagon}")


if __name__ == "__main__":
    task_4()
