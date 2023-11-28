from src.sum import Solution


def test_0_sum_iteration_0():
    result = Solution.sum_iteration_0(5, 3)
    expected = 8
    assert result == expected, f"Expected {expected}, but got {result}"
