"""

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where
it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self._searchInsert(nums, target, 0, len(nums) - 1)

    def _searchInsert(self, nums, target, left, right):
        if left > right:
            return left

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self._searchInsert(nums, target, left, mid - 1)
        else:
            return self._searchInsert(nums, target, mid + 1, right)



if __name__ == "__main__":
    solution = Solution()
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
