import logging


class MergeSort:
    def __init__(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def sort(self, arr: list[int]) -> list[int]:
        if len(arr) > 1:
            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]
            self.sort(left)
            self.sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        logging.debug(arr)
        return arr


if __name__ == "__main__":
    arr = [2, 0, 1, 5, 3, 1, 6, 4, 10]
    merge = MergeSort()
    merge.sort(arr)
