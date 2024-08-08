"""

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
    print('Test case 1 passed')

    l1 = ListNode(9, ListNode(9, ListNode(9)))
    l2 = ListNode(1)
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 0
    assert result.next.val == 0
    assert result.next.next.val == 0
    assert result.next.next.next.val == 1
    print('Test case 2 passed')

    l1 = ListNode(2, ListNode(4))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 5
    print('Test case 3 passed')

    l1 = ListNode(1)
    l2 = ListNode(9)
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 0
    assert result.next.val == 1
    print('Test case 4 passed')

    l1 = ListNode(0)
    l2 = ListNode(1, ListNode(2))
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 1
    assert result.next.val == 2
    print('Test case 5 passed')

    l1 = ListNode(3, ListNode(2, ListNode(1)))
    l2 = ListNode(3, ListNode(2, ListNode(1)))
    result = solution.addTwoNumbers(l1, l2)
    assert result.val == 6
    assert result.next.val == 4
    assert result.next.next.val == 2
    print('Test case 6 passed')
