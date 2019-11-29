# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。 题意'''
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # co'p'y先遍历获取全部，中序遍历从小到大
        l = []
        result = 0
        left = 0
        right = 0
        self.inorder(root, l)  # self要写
        print(l)
        for i, val in enumerate(l):
            if (val == L):
                left = i
            if (val == R):
                right = i
                break
        return sum(l[left:right + 1])

    def inorder(self, root, result):
        if (root):
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)
