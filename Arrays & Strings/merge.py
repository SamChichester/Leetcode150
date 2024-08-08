"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set to 0
and should be ignored. nums2 has a length of n.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        a = m - 1
        b = n - 1
        last_index = m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[last_index] = nums1[a]
                a -= 1
            else:
                nums1[last_index] = nums2[b]
                b -= 1

            last_index -= 1


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    solution.merge(nums1, m, nums2, n)

    assert nums1 == [1, 2, 2, 3, 5, 6]
    assert len(nums1) == 6

