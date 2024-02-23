import numpy as np
import pytest

from Matrix_Vectors.matrix import Matrix


@pytest.fixture()
def matx():
    matrix = Matrix()
    return matrix


class TestMatrix:
    @classmethod
    def test_matrix_sum(cls, matx: Matrix) -> None:
        assert (matx.matrix_sum(np.array([1, 4, 8]), np.array([10, 3, 6])) == np.array([11, 7, 14])).all()

    @classmethod
    def test_matrix_mult(cls, matx: Matrix) -> None:
        assert (matx.matrix_mult(np.array([[1, 8], [2, 5]]), np.array([[5, 6], [10, 9]])) == [[85, 78], [60, 57]]).all()
