"""

Given an integer x, return true if x is a
palindrome, and false otherwise.

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x % 10 == 0 and x != 0) or x < 0:
            return False

        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10

        return x == y or x == y // 10

        # x = str(x)
        #
        # left = 0
        # right = len(x) - 1
        #
        # while left < right:
        #     if x[left] != x[right]:
        #         return False
        #     left += 1
        #     right -= 1
        #
        # return True




if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(12321)
    assert not(solution.isPalindrome(-121))
    assert not(solution.isPalindrome(10))
