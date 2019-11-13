# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None: return True
        print(self.maxDepth(root.left))
        print(self.maxDepth(root.right))
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

        # copy类似
        # def height(node):
        #    if not node:
        #        return 0
        #    return 1 + max(height(node.left), height(node.right))
        # if not root:
        #    return True
        # return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)