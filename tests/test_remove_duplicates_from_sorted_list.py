from src.remove_duplicates_from_sorted_list import Node
from src.remove_duplicates_from_sorted_list import Solution


def test_remove_duplicates_from_sorted_list_iteration_0():
    first_node_0 = Node(1)
    second_node_0 = Node(1)
    third_node_0 = Node(2)
    first_node_0.next = second_node_0
    second_node_0.next = third_node_0
    third_node_0.next = None

    first_result = Solution.remove_duplicates_from_sorted_list_iteration_0(first_node_0)
    first_expected = 1
    assert first_result.value == first_expected, f"Expected {first_expected}, but got {first_result}"
