from typing import List

class Solution:

    def twoSumFirst(self, nums: List[int], target: int) -> List[int]:
        """
        Solution №1: BruteForce.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return []
    
    def twoSumSecond(self, nums: List[int], target: int) -> List[int]:
        """
        Solution №2: BruteForce number 2.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[i] == nums[j] and i != j:
                    return [i, j]
        return []

    def twoSumThird(self, nums: List[int], target: int) -> List[int]:
        """
        Solution №2: Two-pass Hash Table
        """
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashMap and hashMap[result] != i:
                return [i, hashMap[result]]

        return []
    
    def twoSumFour(self, nums: List[int], target: int) -> List[int]:
        """
        Solution №3: One-pass Hash Table
        """
        hashMap = {}
        for i in range(len(nums)):
            result = target - nums[i]
            
            if result in hashMap:
                return [hashMap[result], i]
            
            hashMap[nums[i]] = i    
        return []
    

    