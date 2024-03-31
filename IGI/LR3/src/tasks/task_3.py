from utils import task_decorator

@task_decorator
def task_3():
    """
    This function takes a string as input and returns the number of non-whitespace characters in the string.

    Input:
        line (str): The input string

    Prints:
        int: The number of non-whitespace characters in the input string
    """
    line = input()
    
    count = len([0 for c in line if c.isspace() is False])
        
    print(count)
    