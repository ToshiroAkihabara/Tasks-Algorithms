import random
from twoSum import Solution

def generateRandomValues():
    randomNums = [random.randint(1,5) for i in range(1,10)]
    randomTarget = random.randint(1,20) 
    return randomNums, randomTarget

def main():
    staticNums = [2, 1, 7, 8, 10, 3, 2, 5, 4, 9]
    staticTarget = 5
    solution = Solution()
    solutionFirst = solution.twoSumFirst(staticNums, staticTarget)
    solutionSecond = solution.twoSumSecond(staticNums, staticTarget)
    solutionThird = solution.twoSumThird(staticNums, staticTarget)
    solutionFour = solution.twoSumFour(staticNums, staticTarget)
    
    print(f"1.solutionFirst: {solutionFirst}\n2.solutionSecond: {solutionSecond}\n3.solutionThird: {solutionThird}\n4.solutionFour: {solutionFour}")

if __name__ == "__main__":
    main()
