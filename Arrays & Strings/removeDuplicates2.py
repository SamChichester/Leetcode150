"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place
such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead
have the result be placed in the first part of the array nums. More formally, if there are k elements
after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array
in-place with O(1) extra memory.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        j = 0

        for i in range(len(nums)):
            if j < 2 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 1, 1, 2, 2, 3]
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    k = solution.removeDuplicates(nums1)
    assert k == 5
    assert nums1[:5] == [1, 1, 2, 2, 3]

    k = solution.removeDuplicates(nums2)
    assert k == 7
    assert nums2[:7] == [0, 0, 1, 1, 2, 3, 3]