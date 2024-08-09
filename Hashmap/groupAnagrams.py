"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]

        return list(anagrams.values())


if __name__ == "__main__":
    solution = Solution()
    assert solution.groupAnagrams([""]) == [[""]]
    assert solution.groupAnagrams(["a"]) == [["a"]]
