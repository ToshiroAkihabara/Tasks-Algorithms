import logging


class MergeTwoArr:
    """
    Merge two sorted arrays into one piece 
    """

    def __init__(self, arr_one: list[int], arr_two: list[int]) -> None:
        logging.basicConfig(level=logging.DEBUG)
        self.arr_one = arr_one
        self.arr_two = arr_two

    def merge(self) -> list[int]:
        i, j = 0, 0
        res = []
        while i < len(self.arr_one) and j < len(self.arr_two):
            if self.arr_one[i] < self.arr_two[j]:
                res.append(self.arr_one[i])
                i += 1
            else:
                res.append(self.arr_two[j])
                j += 1
        if i < len(self.arr_one):
            res.append(self.arr_one[i])
            i += 1
        elif j < len(self.arr_two):
            res.append(self.arr_two[j])
            j += j

        return res

