"""

You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height) ** 2

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            if min(height[left], height[right]) * (right - left) > max_area:
                max_area = min(height[left], height[right]) * (right - left)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    solution = Solution()
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height1) == 49
    height2 = [1, 1]
    assert solution.maxArea(height2) == 1
