import pytest

from Matrix_Vectors.matrix import Matrix
from Matrix_Vectors.vectors import VectorList, VectorNumpy


@pytest.fixture()
def matx():
    matrix = Matrix()
    return matrix


@pytest.fixture()
def vec_num() -> VectorNumpy:
    vector_numpy = VectorNumpy()
    return vector_numpy


@pytest.fixture()
def vec_list() -> VectorList:
    vector_list = VectorList()
    return vector_list
