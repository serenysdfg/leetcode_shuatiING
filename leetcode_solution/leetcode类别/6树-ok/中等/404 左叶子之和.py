# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isleaf(root):
            if not root: return False
            if not root.left and not root.right:
                return True

        if not root: return 0
        res = 0
        if isleaf(root.left):
            res += root.left.val
        else:
            res += self.sumOfLeftLeaves(root.left)
        if root.right:
            res += self.sumOfLeftLeaves(root.right)
        return res
