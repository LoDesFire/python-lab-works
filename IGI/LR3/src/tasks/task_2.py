from utils import input_with_check, task_decorator


@task_decorator
def task_2():
    """
    This function prompts the user to enter a series of numbers until the user enters the number 1. 
    The function then prints the largest number entered.
    """
    num = None
    max_num = None
    while True:
        num = input_with_check(int)
        if num == 1:
            break
        max_num = max(max_num, num) if max_num is not None else num
    
    print(f"Maximum number is {max_num}")
    