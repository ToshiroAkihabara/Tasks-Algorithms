import logging


class Heapsort:
    def __init__(self, arr: list[int]) -> None:
        logging.basicConfig(level=logging.DEBUG)
        self.arr = arr
        
    def heapify(self, arr, heap_size, root_index) -> None:
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2
        
        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child
        
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child
            
        if largest != root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            self.heapify(arr, heap_size, largest)
    
    def sort(self) -> None:
        n = len(self.arr)
        for i in range(n, -1, -1):
            self.heapify(self.arr, n, i)
        
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(self.arr, i, 0)
        
        logging.debug(self.arr)
