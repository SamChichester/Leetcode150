"""

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

"""
from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []

        for i in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[i], 0, i))

        results = []
        while heap and len(results) < k:
            pair_sum, i, j = heapq.heappop(heap)
            results.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return results


if __name__ == "__main__":
    solution = Solution()
    assert solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
