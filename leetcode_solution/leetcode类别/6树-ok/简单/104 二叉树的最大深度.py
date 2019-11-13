# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #copy
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 #递归+1，最下面的节点是root加上就好