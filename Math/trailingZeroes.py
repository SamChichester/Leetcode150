"""

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        factorial = 1
        for num in range(1, n + 1):
            factorial *= num

        factorial = str(factorial)
        i = -1
        while factorial[i] == '0':
            i -= 1

        return abs(i + 1)


if __name__ == "__main__":
    solution = Solution()
    assert solution.trailingZeroes(0) == 0
    assert solution.trailingZeroes(3) == 0
    assert solution.trailingZeroes(5) == 1
