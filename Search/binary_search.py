import logging


class Logger:
    def __init__(self) -> None:
        logging.basicConfig(level=logging.DEBUG)


class Search(Logger):
    @classmethod
    def binary_search_recursion(cls, arr: list[int], target: int, first_index: int, last_index: int) -> int:
        if first_index <= last_index:
            middle_index = (first_index + last_index) // 2
            if arr[middle_index] == target:
                logging.debug(f"{arr[middle_index]} in position {middle_index}")
                return middle_index
            elif arr[middle_index] > target:
                return cls.binary_search_recursion(arr, target, first_index, middle_index - 1)
            elif arr[middle_index] < target:
                return cls.binary_search_recursion(arr, target, middle_index + 1, last_index)
        else:
            logging.debug("Doesn't appear in the arr")

    @classmethod
    def binary_search_linear(cls, arr: list[int], target: int, first_index: int, last_index: int) -> int:
        if first_index <= last_index:
            middle_index = (first_index + last_index) // 2
            if arr[middle_index] == target:
                logging.debug(f"{arr[middle_index]} in position {middle_index}")
                return middle_index
            elif arr[middle_index] > target:
                last_index = middle_index - 1
            elif arr[middle_index] < target:
                first_index = middle_index + 1
        else:
            logging.debug("Doesn't appear in the arr")


if __name__ == "__main__":
    arr = [2, 5, 10, 11, 15, 21, 33, 56]
    target = 10
    s = Search()
    s.binary_search_recursion(arr, target, 0, len(arr))
    s.binary_search_linear(arr, target, first_index=0, last_index=len(arr))
