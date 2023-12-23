from src.path_crossing import Solution


def test_0_path_crossing_iteration_0():
    first_result = Solution.path_crossing_iteration_0("NES")
    first_expected = False
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"


def test_1_path_crossing_iteration_0():
    first_result = Solution.path_crossing_iteration_0("NESWW")
    first_expected = True
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"
