# https://leetcode.com/problems/merge-two-sorted-lists/

class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.next = None


class Solution:

    # Best solution that I discovered. It basically utilizes pointers to save up on space.
    # Elements are updated in their places.
    @staticmethod
    def merge_two_sorted_lists_iteration_0(first: [Node], second: [Node]) -> [Node]:
        head = Node()
        current = head

        while first and second:
            if first.value < second.value:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next

            current = current.next

        current.next = first or second
        return head.next
