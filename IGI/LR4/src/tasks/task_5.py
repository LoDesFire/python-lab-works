from src.task_5 import MatrixOperator


def task_5():
    """Launching task 5"""

    mop = MatrixOperator()
    mop.generateMatrix(4, 3)
    print("Matrix before:")
    print(mop.matrix)
    mop.insert_raw_after_the_raw_with_min_element()
    print("\nMatrix after insertion:")
    print(mop.matrix)

    print(f"\nMedian (NP method): {mop.calculateMedianNp()}")
    print(f"Median: {mop.calculateMedian()}")


if __name__ == "__main__":
    task_5()
