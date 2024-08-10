"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        return self._isHappy(n)

    def _isHappy(self, n, previous_nums=None):
        if previous_nums is None:
            previous_nums = set()

        if n in previous_nums:
            return False

        if n == 1:
            return True

        previous_nums.add(n)

        n = str(n)
        total = 0
        for digit in n:
            total += int(digit) ** 2

        return self._isHappy(total, previous_nums)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isHappy(19)
    assert not(solution.isHappy(2))
