# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if node is None: return
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)
        invert(root)

        return root