"""

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1

        return right

if __name__ == "__main__":
    solution = Solution()
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2
