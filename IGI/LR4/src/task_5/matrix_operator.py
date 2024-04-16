import numpy
import numpy as np


class MatrixOperator:
    """Class for operating with random matrix."""

    def __init__(self):
        self.__matrix = np.ndarray([0, 0])

    def generateMatrix(self, a: int, b: int):
        self.__matrix = np.random.rand(a, b)

    def __str__(self):
        for row in self.__matrix:
            print(row)

    def insert_raw_after_the_raw_with_min_element(self):
        minimal = 0
        for index in range(0, self.__matrix.shape[0]):
            if self.__matrix[index, 0] < self.__matrix[minimal, 0]:
                self.__matrix = numpy.insert(self.__matrix, index + 1, self.__matrix[0], axis=0)
                break

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, new_matrix):
        self.__matrix = new_matrix

    def calculateMedianNp(self):
        return numpy.median(self.__matrix)

    def calculateMedian(self):
        r, c = self.__matrix.shape
        amount = r * c
        vals = numpy.sort(self.__matrix.reshape(amount))
        if amount % 2 == 0:
            return numpy.take(vals, [amount // 2, amount // 2 - 1]).mean()
        else:
            return vals[amount // 2]
