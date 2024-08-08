"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
that each unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order
they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums3 = [-1, 0, 0, 0, 0, 3, 3]

    solution.removeDuplicates(nums1)
    solution.removeDuplicates(nums2)
    solution.removeDuplicates(nums3)

    assert nums1[:2] == [1, 2]
    assert nums2[:5] == [0, 1, 2, 3, 4]
    assert nums3[:3] == [-1, 0, 3]
