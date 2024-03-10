# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional


class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.next = None


class Solution:

    @staticmethod
    def remove_duplicates_from_sorted_list_iteration_0(head: Optional[Node]) -> Optional[Node]:
        current = head

        while current is not None and current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

        return head
