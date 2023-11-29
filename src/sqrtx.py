# https://leetcode.com/problems/sqrtx/
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

class Solution:

    # Uses Newton's method to calculate square root of given number.
    @staticmethod
    def sqrtx_iteration_0(number: int) -> int:
        if number == 0:
            return 0

        # The maximum difference allowed between given number and estimate.
        tolerance = 0.00001

        estimate = number
        while True:
            root = 0.5 * (estimate + (number / estimate))
            difference = root - estimate

            if difference < 0:
                difference *= -1

            if difference < tolerance:
                break

            estimate = root

        # Python just lowers the root during casting.
        return int(root)
