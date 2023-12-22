from src.best_time_to_buy_and_sell_stock import Solution


def test_0_bttbass_iteration_0():
    first_result = Solution.best_time_to_buy_and_sell_stock_iteration_0([5, 3, 1, 4, 8])
    first_expected = 7
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"


def test_1_bttbass_iteration_0():
    second_result = Solution.best_time_to_buy_and_sell_stock_iteration_0([3, 1])
    second_expected = 0
    assert second_result == second_expected, f"Expected {second_expected}, but got {second_result}"


def test_2_bttbass_iteration_0():
    third_result = Solution.best_time_to_buy_and_sell_stock_iteration_0([])
    third_expected = 0
    assert third_result == third_expected, f"Expected {third_result}, but got {third_expected}"


def test_0_bttbass_iteration_1():
    first_result = Solution.best_time_to_buy_and_sell_stock_iteration_1([5, 3, 1, 4, 8])
    first_expected = 7
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"


def test_1_bttbass_iteration_1():
    second_result = Solution.best_time_to_buy_and_sell_stock_iteration_1([3, 1])
    second_expected = 0
    assert second_result == second_expected, f"Expected {second_expected}, but got {second_result}"


def test_2_bttbass_iteration_1():
    third_result = Solution.best_time_to_buy_and_sell_stock_iteration_1([])
    third_expected = 0
    assert third_result == third_expected, f"Expected {third_result}, but got {third_expected}"
