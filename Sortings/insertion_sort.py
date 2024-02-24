def insertion_sort(arr: list[int]) -> list[int]:
    """
    Worst: O(n2)
    """
    for j in range(1, len(arr)):
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr
