from math import asin, factorial
from utils import input_with_check, task_decorator

MAX_ITERATIONS = 500

@task_decorator
def task_1():
    """

    This function calculates the arcsine integral of x using the Gauss-Hermite quadrature formula.
    The function takes the following inputs:
        eps (float): the desired precision of the approximation
        x (float): the argument of the arcsine function

    The function returns the number of iterations required to achieve the desired precision.

    """
    eps = input_with_check(float, "eps", max_value=0.11)
    x = input_with_check(float, "x", min_value=-1.0, max_value=1.0)
    
    sum = 0
    iter_count = 0
    arcsin_math = asin(x)
    
    while abs(sum - arcsin_math) > eps and iter_count < MAX_ITERATIONS:
        sum += factorial(2 * iter_count) / (4 ** iter_count * factorial(iter_count) ** 2 * (2 * iter_count + 1)) * x ** (2 * iter_count + 1) 
        iter_count += 1
    
    print("-" * 121)
    print('|\tx\t|\tn\t|\t\tf(x)\t\t|\t\tmath f(x)\t\t|\teps\t|')
    print("-" * 121)
    print(f'|\t{x:.2f}\t|\t{iter_count}\t|\t{sum:.15f}\t|\t{arcsin_math:.15f}\t\t|\t{eps}\t|')
    print("-" * 121)
    