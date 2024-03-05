from geometric_lib import circle, square

def main():
    print("Enter the side length: ", end="")
    side_length = int(input())

    print(f"Area of square: {square.area(side_length)}")

    print(f"Area of inscribed circle: {circle.area(side_length / 2)}")


if __name__ == "__main__":
    main()