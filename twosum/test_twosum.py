import unittest
from twosum import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):

        input_list = [2, 7, 11, 15]
        input_target = 9
        desired_output = [0, 1]
        result = self.solution.twoSum(input_list, input_target)
        self.assertEqual(result, desired_output)

        input_list = [3, 2, 4]
        input_target = 6
        desired_output = [1, 2]
        result = self.solution.twoSum(input_list, input_target)
        self.assertEqual(result, desired_output)

        input_list = [3, 3]
        input_target = 6
        desired_output = [0, 1]
        result = self.solution.twoSum(input_list, input_target)
        self.assertEqual(result, desired_output)

        input_list = [3, 2, 4, 1, 9]
        input_target = 12
        desired_output = [0, 4]
        result = self.solution.twoSum(input_list, input_target)
        self.assertEqual(result, desired_output)

if __name__ == "__main__":
    unittest.main()
