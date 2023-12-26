# https://leetcode.com/problems/single-number/

class Solution:

    # O(n) time and O(n) space complexity.
    @staticmethod
    def single_number_iteration_0(numbers: list[int]) -> int:
        # Create the map.
        occurrence_map = {}

        # Store the occurrence in map.
        for number in numbers:
            if number in occurrence_map:
                occurrence_map[number] += 1
            else:
                occurrence_map[number] = 1

        # Find out the occurrence with '1' frequency.
        for occurrence in occurrence_map:
            if occurrence_map[occurrence] == 1:
                return occurrence

        # Return an invalid value.
        return -1
