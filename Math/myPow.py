"""

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


if __name__ == "__main__":
    solution = Solution()
    assert solution.myPow(2.00000, 10) == 1024.00000
    assert solution.myPow(2.10000, 3) == 9.26100
    assert solution.myPow(2.00000, -2) == 0.25000