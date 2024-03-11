from src.remove_duplicates_from_sorted_array import Solution


def test_remove_duplicates_from_sorted_array_iteration_0():
    first_array = [1, 1, 2, 3, 4, 4, 5]
    first_result = Solution.remove_duplicates_from_sorted_array_iteration_0(first_array)
    first_expected = 5
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"
