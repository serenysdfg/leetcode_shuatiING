# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # copy迭代
        res = []
        if not root:
            return res

        stack = []
        node = root
        while node or (len(stack) > 0):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res
        # 递归简单
        # ret = []
        # def dp(root):
        #     if root != None:
        #         dp(root.left)
        #         ret.append(root.val)
        #         dp(root.right)
        # dp(root)
        # return ret