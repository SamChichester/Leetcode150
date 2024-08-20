"""

Given the head of a linked list, rotate the list to the right by k places.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 1

        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1

        tail.next = head

        k %= length

        for _ in range(length - k):
            head = head.next
            tail = tail.next

        tail.next = None

        return head


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = solution.rotateRight(head, 2)
    for i in [4, 5, 1, 2, 3]:
        assert new_head.val == i
        new_head = new_head.next
    assert not new_head

    head = ListNode(0, ListNode(1, ListNode(2)))
    new_head = solution.rotateRight(head, 4)
    for i in [2, 0, 1]:
        assert new_head.val == i
        new_head = new_head.next
    assert not new_head
