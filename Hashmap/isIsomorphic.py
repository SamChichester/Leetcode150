"""

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}

        for sc, tc in zip(s, t):
            if (sc in s_chars and s_chars[sc] != tc) or (tc in t_chars and t_chars[tc] != sc):
                return False
            s_chars[sc] = tc
            t_chars[tc] = sc

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isIsomorphic('egg', 'add')
    assert not(solution.isIsomorphic('foo', 'bar'))
    assert solution.isIsomorphic('paper', 'title')
