"""

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in s.

"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        if len(pattern) != len(s_words):
            return False

        p_dict = {}
        s_dict = {}

        for sw, pc in zip(pattern, s_words):
            if (sw in s_dict and s_dict[sw] != pc) or (pc in p_dict and p_dict[pc] != sw):
                return False
            s_dict[sw] = pc
            p_dict[pc] = sw

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.wordPattern('abba', 'dog cat cat dog')
    assert not(solution.wordPattern('abba', 'dog cat cat fish'))
    assert not(solution.wordPattern('aaaa', 'dog cat cat dog'))
