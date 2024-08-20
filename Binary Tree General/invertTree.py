"""

Given the root of a binary tree, invert the tree, and return its root.

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    new_root = solution.invertTree(root)
    assert new_root.left.left.val == 9
    assert new_root.left.right.val == 6
    assert new_root.left.val == 7
    assert new_root.val == 4
    assert new_root.right.val == 2
    assert new_root.right.left.val == 3
    assert new_root.right.right.val == 1
