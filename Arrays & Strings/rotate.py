"""

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        k %= n
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums1, 1)
    assert nums1 == [7, 1, 2, 3, 4, 5, 6]
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums2, 3)
    assert nums2 == [5, 6, 7, 1, 2, 3, 4]

