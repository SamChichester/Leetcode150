"""

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_linked_list(head, k):
            prev_node = None
            curr_node = head

            for _ in range(k):
                next_node = curr_node.next
                curr_node.next = prev_node

                prev_node = curr_node
                curr_node = next_node

            return prev_node

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while length >= k:
            current = prev.next
            next_segment = current
            for _ in range(k):
                next_segment = next_segment.next
            reversed_segment = reverse_linked_list(current, k)

            prev.next = reversed_segment
            current.next = next_segment
            prev = current

            length -= k

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = solution.reverseKGroup(head, 2)
    for i in [2, 1, 4, 3, 5]:
        assert new_head.val == i
        new_head = new_head.next
    assert not new_head

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = solution.reverseKGroup(head, 3)
    for i in [3, 2, 1, 4, 5]:
        assert new_head.val == i
        new_head = new_head.next
    assert not new_head
