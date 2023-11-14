import unittest
from twoSum import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.nums = [2, 1, 7, 8, 10, 3, 2, 5, 4, 9]
        self.target = 5
        self.result = [0,5]
 
    def test_twoSumFirst(self):
        self.assertEqual(self.solution.twoSumFirst(self.nums, self.target), self.result)

    def test_twoSumSecond(self):
        self.assertEqual(self.solution.twoSumSecond(self.nums, self.target), self.result)

    def test_twoSumThird(self):
        self.assertEqual(self.solution.twoSumThird(self.nums, self.target), self.result)

    def test_twoSumFour(self):
        self.assertEqual(self.solution.twoSumFour(self.nums, self.target), self.result)


if __name__ == "__main__":
    unittest.main()