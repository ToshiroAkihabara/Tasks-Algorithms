from contextlib import nullcontext as does_not_raises

import numpy as np
import pytest

from Matrix_Vectors.matrix import Matrix


@pytest.fixture()
def matx():
    matrix = Matrix()
    return matrix


class TestMatrix:
    @pytest.mark.parametrize(
        "matrix_1, matrix_2, expected_result, exception",
        [
            (
                np.array([[1, 8], [2, 5]], dtype=int),
                np.array([[5, 6], [10, 9]], dtype=int),
                np.array([[85, 78], [60, 57]], dtype=int),
                does_not_raises(),
            ),
            (
                np.array([[1, 8], [2, 5]], dtype=int),
                np.array([[5, 6], [10, 9], [5, 2]], dtype=int),
                np.array([[85, 78], [60, 57]], dtype=int),
                pytest.raises(ValueError),
            ),
            (
                [[1, 8], [2, 5]],
                [[5, 6], [10, 9]],
                [[85, 78], [60, 57]],
                pytest.raises(ValueError),
            ),
        ],
    )
    def test_matrix_mult(
        self, matx: Matrix, matrix_1, matrix_2, expected_result, exception
    ) -> None:
        with exception:
            assert (matx.matrix_mult(matrix_1, matrix_2) == expected_result).all()

    @pytest.mark.parametrize(
        "matrix_1, matrix_2, expected_result, exception",
        [
            (
                np.array([1, 4, 8], dtype=int),
                np.array([10, 3, 6], dtype=int),
                np.array([11, 7, 14], dtype=int),
                does_not_raises(),
            ),
            (
                [6, 10, 23],
                np.array([2, 14, 9], dtype=int),
                np.array([8, 24, 32], dtype=int),
                pytest.raises(ValueError),
            ),
        ],
    )
    def test_matrix_sum(
        self, matx: Matrix, matrix_1, matrix_2, expected_result, exception
    ) -> None:
        with exception:
            assert (matx.matrix_sum(matrix_1, matrix_2) == expected_result).all()
