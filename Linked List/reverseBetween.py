"""

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next

        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = solution.reverseBetween(head, 2, 4)
    for i in [1, 4, 3, 2, 5]:
        assert new_head.val == i
        new_head = new_head.next

    assert not new_head
