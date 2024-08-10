"""

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.

"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if i - nums_dict[nums[i]] <= k:
                    return True
            nums_dict[nums[i]] = i


if __name__ == "__main__":
    solution = Solution()
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
