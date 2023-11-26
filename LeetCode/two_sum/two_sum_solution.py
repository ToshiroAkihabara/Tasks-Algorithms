from typing import Dict, List


class TwoSumSolution:
    """pytest LeetCode/tests/test_two_sum.py -v"""

    def two_sum_first(self, nums: List[int], target: int) -> List[int]:
        """Solution №1: BruteForce."""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return []

    def two_sum_second(self, nums: List[int], target: int) -> List[int]:
        """Solution №2: BruteForce number 2."""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[i] == nums[j] and i != j:
                    return [i, j]
        return []

    def two_sum_third(self, nums: List[int], target: int) -> List[int]:
        """Solution №2: Two-pass Hash Table"""
        hashMap: Dict[int, int] = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashMap and hashMap[result] != i:
                return [i, hashMap[result]]

        return []

    def two_sum_four(self, nums: List[int], target: int) -> List[int]:
        """Solution №3: One-pass Hash Table"""
        hashMap: Dict[int, int] = {}
        for i in range(len(nums)):
            result = target - nums[i]

            if result in hashMap:
                return [hashMap[result], i]

            hashMap[nums[i]] = i
        return []
