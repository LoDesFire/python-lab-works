from tasks import task_1, task_2, task_3, task_4, task_5
from utils import input_with_check
import os

def main():
    while True:
        os.system('clear')
        print("1. Task 1")
        print("2. Task 2")
        print("3. Task 3")
        print("4. Task 4")
        print("5. Task 5")
        print("0. Exit")
        choice = input_with_check(int)
        os.system('clear')
        match choice:
            case 1:
                task_1()
            case 2:
                task_2()
            case 3:
                task_3()
            case 4:
                task_4()
            case 5:
                task_5()
            case 0:
                exit()
            case _:
                print(f"Invalid choice: {choice}")

if __name__ == '__main__':
    main()