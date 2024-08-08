"""

You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while digits[i] == 9:
            if i == 0:
                digits.append(0)
                digits[i] = 1
                return digits
            digits[i] = 0
            i -= 1
        digits[i] += 1

        return digits


if __name__ == "__main__":
    solution = Solution()
    # assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    # assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    # assert solution.plusOne([8, 9, 9]) == [9, 0, 0]
    assert solution.plusOne([9]) == [1, 0]
