import numpy as np


class Matrix:
    @classmethod
    def matrix_sum(
            cls, matrix_1: np.array([], int),
            matrix_2: np.array([], int)
    ) -> np.array([], int):
        return matrix_1 + matrix_2

    @classmethod
    def matrix_mult(
            cls,
            matrix_1: np.array([], int),
            matrix_2: np.array([], int)
    ) -> np.array([], int):
        if len(matrix_1[0]) == len(matrix_2[:, 0]):
            return np.dot(matrix_1, matrix_2)
        else:
            raise ValueError(f"The length {matrix_1} of row not equal the length {matrix_2} of column")


