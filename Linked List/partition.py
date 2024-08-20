"""

Given the head of a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode()
        after_head = ListNode()

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    new_head = solution.partition(head, 3)
    for i in [1, 2, 2, 4, 3, 5]:
        assert new_head.val == i
        new_head = new_head.next
    assert not new_head

    head = ListNode(2, ListNode(1))
    new_head = solution.partition(head, 2)
    for i in [1, 2]:
        assert new_head.val == i
        new_head = new_head.next
    assert not new_head
