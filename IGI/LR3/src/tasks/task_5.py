from typing import List
from utils import input_with_check, task_decorator

@task_decorator
def task_5():
    """
    This function takes a list of numbers as input and returns the multiplication of the even numbers 
    and the sum of numbers between the first and the last zero-values.
    """
    list_len = input_with_check(int, "list length", max_value=500)
    num_list: List[float] = [input_with_check(float) for i in range(list_len)]
    
    result = 1
    for index in range(1, len(num_list), 2):
        result *= num_list[index]
    
    first = None
    for index in range(0, len(num_list)):
        if num_list[index] == 0:
            first = index
            break
    
    last = None
    for index in range(len(num_list) - 1, -1, -1):
        if num_list[index] == 0:
            last = index
            break
    
    sum = 0
    if first is not None and last is not None:
        for index in range(first, last):
            sum += num_list[index]
        
    print(f"Multiplication result: {result}\nSum result: {sum}")