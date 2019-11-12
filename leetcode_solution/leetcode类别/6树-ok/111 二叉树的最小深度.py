# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # copy
        # 解题思路：分几种情况考虑：1，树为空，则为0。
        # 2，根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的（最小深度+1）。
        #
        # 3，如果根节点的左子树和右子树都存在，则返回值为（左右子树的最小深度的较小值+1）。

        if not root:  # 一旦有叶节点，就返回0
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1

        if not root.right:  # 只存在左子树
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1