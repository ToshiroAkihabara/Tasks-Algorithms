import numpy as np


class Matrix:
    @classmethod
    def matrix_sum(
        cls, matrix_1: np.array([], int), matrix_2: np.array([], int)
    ) -> np.array([], int):
        if isinstance(matrix_1, np.ndarray) and isinstance(matrix_2, np.ndarray):
            return matrix_1 + matrix_2
        else:
            raise ValueError("Unsupported type. Convert data to numpy.ndarray")

    @classmethod
    def matrix_mult(
        cls, matrix_1: np.array([], dtype=int), matrix_2: np.array([], dtype=int)
    ) -> np.array([], int):
        if isinstance(matrix_1, np.ndarray) and isinstance(matrix_2, np.ndarray):
            if len(matrix_1[0]) == len(matrix_2[:, 0]):
                try:
                    result = np.dot(matrix_1, matrix_2)
                    return result
                except ValueError:
                    raise ValueError("Data type must provide an itemsize")
            else:
                raise ValueError(
                    f"The length {matrix_1} of row not equal the length {matrix_2} of column"
                )
        else:
            raise ValueError("Unsupported type. Convert data to numpy.ndarray")
