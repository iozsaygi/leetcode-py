# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:

    # O(n) solution with index tracking.
    @staticmethod
    def remove_duplicates_from_sorted_array_iteration_0(numbers: list[int]) -> int:
        current = 1

        for i in range(1, len(numbers)):
            if numbers[i] != numbers[i - 1]:
                numbers[current] = numbers[i]
                current += 1

        return current
