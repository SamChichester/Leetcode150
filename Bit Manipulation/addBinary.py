"""

Given two binary strings a and b, return their sum as a binary string.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    solution = Solution()
    assert solution.addBinary('11', '1') == '100'
    assert solution.addBinary('1010', '1011') == '10101'
