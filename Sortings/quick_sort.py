def quicksort(arr) -> list[int]:
    """
    Worst: O(n2)
    """
    if len(arr) <= 1:
        return arr

    elem = arr[len(arr) // 2]
    left = [i for i in arr if i < elem]
    middle = [i for i in arr if i == elem]
    right = [i for i in arr if i > elem]

    return quicksort(left) + middle + quicksort(right)
