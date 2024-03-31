def input_with_check(input_type: type, value_name: str = None, max_value = None, min_value = None):
    if (type(max_value) != input_type and max_value != None or type(min_value) != input_type and min_value != None):
        raise ValueError(f"max_value and min_value must be of type {input_type.__name__}")
    
    input_text = f"Enter the {input_type.__name__} value{f' {value_name}' if value_name is not None else ''}: "
    while True:
        try:
            val = input_type(input(input_text if value_name is not None else ""))
            
            if max_value is not None and val >= max_value:
                raise ValueError(f"Value {val} is too big. Max value is {max_value}")
            elif min_value is not None and val <= min_value:
                raise ValueError(f"Value {val} is too small. Min value is {min_value}")
            
            return val
        except ValueError:
            if value_name is None:
                print(input_text)
            continue

            

def task_decorator(func):
    def wrapper(*args, **kwargs):
        print("FUNCTION DOCS")
        print(func.__doc__)
        print("/\\"* 60)
        f = func(*args, **kwargs)
        print("/\\"* 60)
        input("Press enter to continue...")
        return f
    return wrapper

