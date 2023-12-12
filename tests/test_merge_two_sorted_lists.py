from src.merge_two_sorted_lists import Solution
from src.linked_list_cycle import Node


def test_0_merge_two_sorted_lists_iteration_0():
    first_node_0 = Node(5)
    second_node_0 = Node(2)
    third_node_0 = Node(4)
    first_node_0.next = second_node_0
    second_node_0.next = third_node_0
    third_node_0.next = None

    first_node_1 = Node(1)
    second_node_1 = Node(7)
    third_node_1 = Node(3)
    first_node_1.next = second_node_1
    second_node_1.next = third_node_1
    third_node_1.next = None

    first_result = Solution.merge_two_sorted_lists_iteration_0(first_node_0, first_node_1)
    first_expected = first_node_1
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"
