"""

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s, len_t = len(s), len(t)

        if len_s == 0:
            return True

        if len_t == 0:
            return False

        i = 0
        for j in range(len_t):
            if t[j] == s[i]:
                i += 1
                if i == len_s:
                    return True
        return False



if __name__ == "__main__":
    solution = Solution()
    s1 = 'abc'
    t = 'ahbgdc'
    assert solution.isSubsequence(s1, t)
    s2 = 'axc'
    assert not(solution.isSubsequence(s2, t))
    s3 = ''
    assert solution.isSubsequence(s3, t)
    s4 = 'b'
    assert solution.isSubsequence(s4, t)
    s5 = 'abb'
    assert solution.isSubsequence(s5, 'abba')