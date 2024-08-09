"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_dict = {}

        for char in magazine:
            letters_dict[char] = letters_dict.get(char, 0) + 1

        for char in ransomNote:
            if letters_dict.get(char, 0) == 0:
                return False
            letters_dict[char] -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    assert not(solution.canConstruct('a', 'b'))
    assert not(solution.canConstruct('aa', 'ab'))
    assert solution.canConstruct('aa', 'aab')
