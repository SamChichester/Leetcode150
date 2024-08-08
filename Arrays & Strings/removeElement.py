"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    assert nums1[:k1] == [2, 2]
    assert k1 == 2

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    assert nums2[:k2] == [0, 1, 3, 0, 4]
    assert k2 == 5
