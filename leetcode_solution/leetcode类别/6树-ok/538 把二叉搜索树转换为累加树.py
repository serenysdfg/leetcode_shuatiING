# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 不太懂
        # 先求树中所有结点值的和sum，然后中序遍历BST，用sum代替之前的结点值，然后更新sum。
        # 因为是平衡二叉树，所以有点的节点的值是大于左边的值。可以从右边开始累加，递归遍历即可。
        self.res = 0

        def dp(root):
            if root != None:
                dp(root.right)  # 先进入最右边的节点
                self.res += root.val
                root.val = self.res
                dp(root.left)

        dp(root)
        return root