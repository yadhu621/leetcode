from typing import List

class Solution:
    """
    A class to represent the solution for twoSum problem

    Methods
    -------
    two_sum(nums, target)
        Returns the solution as a list of integers
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the indices of the numbers that satisfy the solution criteria

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    TARGET = 13
    s = Solution()
    print(s.two_sum(nums, TARGET))
