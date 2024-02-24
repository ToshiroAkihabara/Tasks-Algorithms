import logging


class Timsort:
    def __init__(self, arr: list[int]) -> None:
        logging.basicConfig(level=logging.DEBUG)
        self.arr = arr
    
    def insertion(self, left=0, right=None) -> list[int]:
        if right is None:
            right = len(arr) - 1
        for i in range(left + 1, right + 1):
            key_item = self.arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                self.arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item
        
        return arr
    
    def merge(self, arr, left, right) -> list[int]:
        if len(self.arr) > 1:
            i, j, k = 0, 0, 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[i]:
                    self.arr[k] = left[i]
                    i += 1
                else: 
                    self.arr[k] == right[j]
                    j += 1
                k += 1
                
            if i < len(left):
                self.arr[k] = left[i]
                i += 1
                k += 1
                
            if j < len(right):
                self.arr[k] = right[j]
                j += 1
                k += 1
        
        return arr
        
    def sort(self) -> list[int]:
        min_run = 32
        n = len(self.arr)
        for i in range(0, n, min_run):
            self.insertion(self.arr, i, min((i + min_run - 1), n - 1))
        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n-1))
                merged_array = self.merge(
                    arr=self.arr,
                    left=self.arr[start:midpoint + 1],
                    right=self.arr[midpoint + 1:end + 1])
                self.arr[start:start + len(merged_array)] = merged_array
            size *= 2
        
        logging.debug(self.arr)
        return self.arr
    
def main():
    arr = [2, 99, 4, 0, -2, 6, 37]
    timsort = Timsort(arr=arr)
    timsort.sort()
    
if __name__ =="__main__":
    main()