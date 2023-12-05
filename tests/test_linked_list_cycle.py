from src.linked_list_cycle import Solution
from src.linked_list_cycle import Node


def test_0_llc_iteration_0():
    first_node = Node(0)
    second_node = Node(1)
    third_node = Node(2)
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = None

    first_result = Solution.llc_iteration_0(first_node)
    first_expected = False
    assert first_result == first_expected, f"Expected {first_expected}, but got {first_result}"

    first_node.next = second_node
    second_node.next = third_node
    third_node.next = first_node

    second_result = Solution.llc_iteration_0(first_node)
    second_expected = True
    assert second_result == second_expected, f"Expected {second_expected}, but got {second_result}"
