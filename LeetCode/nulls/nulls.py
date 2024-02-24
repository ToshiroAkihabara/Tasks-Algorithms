import logging
from collections import deque


def nullable1(arr: list[int]) -> list[int]:
    null_arr = []
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            null_arr.append(arr[i])
        else:
            new_arr.append(arr[i])
    return new_arr + null_arr


def nullable2(arr: list[int]) -> list[int]:
    right = [i for i in arr if i == 0]
    left = [i for i in arr if i != 0]
    return left + right


def nullable3(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] == 0:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def nullable_best(arr: list[int]) -> deque[[]]:
    new_arr = deque([])
    for i in arr:
        if i == 0:
            new_arr.append(i)
        else:
            new_arr.appendleft(i)
    return new_arr

