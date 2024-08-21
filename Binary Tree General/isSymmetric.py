"""

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def _isSymmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val) \
                and _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)

        return _isSymmetric(root.left, root.right)


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert solution.isSymmetric(root)
