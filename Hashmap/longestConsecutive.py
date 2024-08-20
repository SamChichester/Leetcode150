"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                current_streak = 1

                while current + 1 in num_set:
                    current += 1
                    current_streak += 1

                max_streak = max(max_streak, current_streak)

        return max_streak


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
