"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = ''.join([char.lower() for char in s if char.isalnum()])
        n = len(filtered)
        for i in range(n // 2):
            if filtered[i] != filtered[(n - 1) - i]:
                return False
        return True



if __name__ == "__main__":
    solution = Solution()
    s1 = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s1)
    s2 = "race a car"
    assert not(solution.isPalindrome(s2))
    s3 = " "
    assert solution.isPalindrome(s3)