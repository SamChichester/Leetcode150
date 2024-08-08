"""

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        intervals = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                if start != nums[i - 1]:
                    intervals.append(f"{start}->{nums[i - 1]}")
                else:
                    intervals.append(f"{start}")
                start = nums[i]

        if start != nums[-1]:
            intervals.append(f"{start}->{nums[-1]}")
        else:
            intervals.append(str(start))

        return intervals


if __name__ == "__main__":
    solution = Solution()
    assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
