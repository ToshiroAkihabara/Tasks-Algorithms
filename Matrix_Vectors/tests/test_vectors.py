import numpy as np
import pytest

from Matrix_Vectors.vectors import VectorList, VectorNumpy


@pytest.fixture()
def vec_num() -> VectorNumpy:
    vector_numpy = VectorNumpy()
    return vector_numpy


@pytest.fixture()
def vec_list() -> VectorList:
    vector_list = VectorList()
    return vector_list


class TestVectorNumpy:
    def test_vector_sum(self, vec_num: VectorNumpy) -> bool:
        assert vec_num.vectors_sum(np.array([2, 3]), np.array([5, 8])) == [7, 11]

    def test_vector_sub(self, vec_num: VectorNumpy) -> bool:
        assert vec_num.vectors_sub(np.array([2, 3]), np.array([5, 8])) == [-3, -5]

    def test_vector_mult(self, vec_num: VectorNumpy) -> bool:
        assert vec_num.vectors_mult(np.array([2, 3]), np.array([5, 8])) == [10, 24]

    def test_vector_div(self, vec_num: VectorNumpy) -> bool:
        assert vec_num.vectors_div(np.array([2, 40]), np.array([2, 8])) == [1, 5]


@pytest.mark.parametrize(
    "vector_1, vector_2",
    [
        ([8, 10], [4, 2])
    ]
)
class TestVectorList:
    def test_vector_sum(
            self,
            vec_list: VectorList,
            vector_1: list[int],
            vector_2: list[int]
    ) -> bool:
        assert vec_list.vectors_sum(vector_1, vector_2) == [12, 12]

    def test_vector_sub(
            self,
            vec_list: VectorList,
            vector_1: list[int],
            vector_2: list[int]
    ) -> bool:
        assert vec_list.vectors_sub(vector_1, vector_2) == [4, 8]

    def test_vector_mult(
            self,
            vec_list: VectorList,
            vector_1: list[int],
            vector_2: list[int]
    ) -> bool:
        assert vec_list.vectors_mult(vector_1, vector_2) == [32, 20]

    def test_vector_div(
            self,
            vec_list: VectorList,
            vector_1: list[int],
            vector_2: list[int]
    ) -> bool:
        assert vec_list.vectors_div(vector_1, vector_2) == [2, 5]