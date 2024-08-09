"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}

        for sc, tc in zip(s, t):
            s_chars[sc] = s_chars.get(sc, 0) + 1
            t_chars[tc] = t_chars.get(tc, 0) + 1

        return s_chars == t_chars


if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram('anagram', 'nagaram')
    assert not(solution.isAnagram('rat', 'car'))
