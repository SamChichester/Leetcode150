"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


if __name__ == "__main__":
    solution = Solution()
    strs1 = ["flower", "flow", "flight"]
    assert solution.longestCommonPrefix(strs1) == 'fl'
    strs2 = ["dog", "racecar", "car"]
    assert solution.longestCommonPrefix(strs2) == ''
