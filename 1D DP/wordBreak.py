"""

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.wordBreak("leetcode", ["leet", "code"])
    assert solution.wordBreak("applepenapple", ["apple", "pen"])
    assert not(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
