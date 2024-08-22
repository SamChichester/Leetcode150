"""

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].

"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        num_jumps = 0
        current_max_reach = 0
        total_max_reach = 0

        for i in range(n - 1):
            total_max_reach = max(total_max_reach, i + nums[i])

            if current_max_reach == i:
                num_jumps += 1
                current_max_reach = total_max_reach

                if current_max_reach >= n - 1:
                    break

        return num_jumps


if __name__ == "__main__":
    solution = Solution()
    assert solution.jump([2, 3, 1, 1, 4]) == 2
    assert solution.jump([2, 3, 0, 1, 4]) == 2
