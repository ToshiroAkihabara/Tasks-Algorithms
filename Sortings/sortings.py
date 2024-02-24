import logging


class Sortings:
    def __init__(self, arr: list[int]) -> None:
        logging.basicConfig(level=logging.DEBUG)
        self.arr = arr
        self.n = len(arr)
    
    def bubble_sort(self) -> list[int]:
        """
        Worst: O(n2)
        """
        for _ in range(self.n-1):
            for i in range(self.n-1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i] 
        return self.arr       
    
    def selection_sort(self) -> list[int]:
        """
        Worst: O(n2)
        """
        for i in range(1, self.n):
            min = i
            for j in range(i + 1, self.n):
                if self.arr[j] < self.arr[min]:
                    min = j
            self.arr[min], self.arr[i] = self.arr[i], self.arr[min]
        return self.arr
    
    def insertion_sort(self) -> list[int]:
        """
        Worst: O(n2)
        """
        for j in range(1, self.n):
            while self.arr[j - 1] > self.arr[j] and j > 0:
                self.arr[j - 1], self.arr[j] = self.arr[j], self.arr[j - 1]
                j -= 1
        return self.arr
    
    def merge_sort(self, arr: list[int]) -> list[int]:
        """
        Worst: O(nlogn)
        """
        # recurse division two sorted lists
        if len(arr) > 1:
            middle = len(arr) // 2
            left = self.merge_sort(arr[:middle])
            right = self.merge_sort(arr[middle:])
        
            # merged two sorted lists
            i, j, k = 0, 0, 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[i]:
                    arr[k] = left[i]
                    i += 1
                else: 
                    arr[k] = right[j]
                    j += 1
                k += 1
                
            if i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                
            if j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
        return arr
    
    def quicksort(self, arr) -> list[int]:
        """
        Worst: O(n2)
        """
        if len(arr) <= 1:
            return arr
        
        elem = arr[len(arr) // 2]
        left = [i for i in arr if i < elem]
        middle = [i for i in arr if i == elem]
        right = [i for i in arr if i > elem]
        
        return self.quicksort(left) + middle + self.quicksort(right)
    
    def counting_sort(self) -> list[int]:
        pass
    
    def binary_insertion_sort(self):
        pass
    
    def radix_sort(self):
        pass
            
                
def main():
    items = [2, -6, -1, 55, 76, 4, 0, 1, 4, 9, 89]
    isort = Sortings(arr=items)
    insertion_sort = isort.insertion_sort()
    bubble_sort = isort.bubble_sort()
    selection_sort = isort.selection_sort()
    merge_sort = isort.merge_sort(arr=items)
    quick_sort = isort.quicksort(arr=items)
    logging.debug(f"Insertion sort: {insertion_sort}")
    logging.debug(f"Bubble sort: {bubble_sort}")
    logging.debug(f"Selection sort: {selection_sort}")
    logging.debug(f"Merge sort: {merge_sort}")
    logging.debug(f"Quick sort: {quick_sort}")

    
if __name__ == "__main__":
    main()