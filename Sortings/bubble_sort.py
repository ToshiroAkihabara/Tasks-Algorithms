def bubble_sort(arr: list[int]) -> list[int]:
    """
    Worst: O(n2)
    """
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
