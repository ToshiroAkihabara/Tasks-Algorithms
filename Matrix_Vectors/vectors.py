import numpy as np


class VectorNumpy:
    @classmethod
    def vectors_sum(
        cls, v1: np.array([], dtype=int), v2: np.array([], dtype=int)
    ) -> np.array([], dtype=int):
        return v1 + v2

    @classmethod
    def vectors_sub(
        cls, v1: np.array([], dtype=int), v2: np.array([], dtype=int)
    ) -> np.array([], dtype=int):
        return v1 - v2

    @classmethod
    def vectors_mult(
        cls, v1: np.array([], dtype=int), v2: np.array([], dtype=int)
    ) -> np.array([], dtype=int):
        return v1 * v2

    @classmethod
    def vectors_div(
        cls, v1: np.array([], dtype=int), v2: np.array([], dtype=int)
    ) -> np.array([], dtype=int):
        return v1 / v2


class VectorList:
    @classmethod
    def vectors_sum(cls, v1: list[int], v2: list[int]) -> list[int]:
        k = []
        i = j = 0
        while i < len(v1) and j < len(v2):
            k.append(v1[i] + v2[j])
            j += 1
            i += 1
        return k

    @classmethod
    def vectors_sub(cls, v1: list[int], v2: list[int]) -> list[int]:
        k = []
        i = j = 0
        while i < len(v1) and j < len(v2):
            k.append(v1[i] - v2[j])
            i += 1
            j += 1
        return k

    @classmethod
    def vectors_mult(cls, v1: list[int], v2: list[int]) -> list[int]:
        k = []
        i = j = 0
        while i < len(v1) and j < len(v2):
            k.append(v1[i] * v2[j])
            i += 1
            j += 1
        return k

    @classmethod
    def vectors_div(cls, v1: list[int], v2: list[int]) -> list[float]:
        k = []
        i = j = 0
        while i < len(v1) and j < len(v2):
            k.append(v1[i] / v2[j])
            i += 1
            j += 1
        return k
