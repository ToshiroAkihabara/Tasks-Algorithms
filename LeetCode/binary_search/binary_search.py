from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle - 1
            if nums[middle] < target:
                high = middle + 1
        return -1
