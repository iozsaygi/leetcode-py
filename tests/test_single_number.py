from src.single_number import Solution


def test_0_single_number_iteration_0():
    first_result = Solution.single_number_iteration_0([2, 2, 1])
    first_expected = 1
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"


def test_1_single_number_iteration_0():
    second_result = Solution.single_number_iteration_0([4, 1, 2, 1, 2])
    second_expected = 4
    assert second_result == second_expected, f"Expected {second_expected}, but got {second_result}"


def test_2_single_number_iteration_0():
    third_result = Solution.single_number_iteration_0([1])
    third_expected = 1
    assert third_result == third_expected, f"Expected {third_expected}, but got {third_result}"
