from src import *


def main():
    while True:
        print()
        task_num = input("Enter the task number: ")
        print()
        match task_num:
            case "1":
                task_1()
            case "2":
                task_2()
            case "3":
                task_3()
            case "4":
                task_4()
            case "5":
                task_5()
            case _:
                print("Try again...")


if __name__ == "__main__":
    main()
