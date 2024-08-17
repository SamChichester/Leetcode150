"""

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        curr_max = 2
        for i in range(n):
            d = {}
            for j in range(n):
                if i != j:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) \
                        if points[j][0] - points[i][0] != 0 else float('inf')
                    d[slope] = d.get(slope, 1) + 1

            curr_max = max(curr_max, max(d.values()))
        return curr_max


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert solution.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
