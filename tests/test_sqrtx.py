from src.sqrtx import Solution


def test_0_sqrtx_iteration_0():
    first_result = Solution.sqrtx_iteration_0(25)
    first_expected = 5
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"

    second_result = Solution.sqrtx_iteration_0(0)
    second_expected = 0
    assert second_result == second_expected, f"Expected {second_expected}, but got {second_result}"

    third_result = Solution.sqrtx_iteration_0(8)
    third_expected = 2
    assert third_result == third_expected, f"Expected {third_expected}, but got {third_result}"
