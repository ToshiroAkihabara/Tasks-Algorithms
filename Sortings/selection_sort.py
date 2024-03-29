def selection_sort(arr: list[int]) -> list[int]:
    """
    Worst: O(n2)
    """
    for i in range(1, len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
