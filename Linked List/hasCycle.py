"""

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == "__main__":
    solution = Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    assert solution.hasCycle(node1)
    print('passed')

    node1 = ListNode(1)
    node2 = ListNode(2)

    node1.next = node2
    node2.next = None

    assert not(solution.hasCycle(node1))
    print('passed')

    assert not(solution.hasCycle(None))
    print('passed')

    node1 = ListNode(1)
    assert not(solution.hasCycle(node1))
    print('passed')

    node1 = ListNode(1)
    node1.next = node1

    assert solution.hasCycle(node1)
    print('passed')
