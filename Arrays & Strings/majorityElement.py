"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1

        for i in nums_dict:
            print(i)
            if nums_dict[i] > (len(nums) // 2):
                return i


if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]

    assert(solution.majorityElement(nums1) == 3)
    assert(solution.majorityElement(nums2) == 2)