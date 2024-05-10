from typing import List


class Solution:
    def contains_dublicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i
            else:
                return True
        return False
