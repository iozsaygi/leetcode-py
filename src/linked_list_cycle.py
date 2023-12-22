# https://leetcode.com/problems/linked-list-cycle/
# https://en.wikipedia.org/wiki/Cycle_detection

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Solution:

    # Solution that uses Floyd's tortoise and hare algorithm.
    @staticmethod
    def linked_list_cycle_iteration_0(head: Node) -> bool:
        if not head or not head.next:
            return False

        tortoise = head
        hare = head.next

        while hare and hare.next:
            if tortoise == hare:
                return True

            tortoise = tortoise.next
            hare = hare.next.next

        return False
