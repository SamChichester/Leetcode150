"""

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word = s.split()[-1]
        return len(last_word)


if __name__ == "__main__":
    solution = Solution()
    s1 = 'Hello World'
    assert solution.lengthOfLastWord(s1) == 5
    s2 = "   fly me   to   the moon  "
    assert solution.lengthOfLastWord(s2) == 4
    s3 = "luffy is still joyboy"
    assert solution.lengthOfLastWord(s3) == 6
