# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.preValue, self.minDiff = 0x7fffffff, 0x7fffffff
        self.inOrder(root)
        return self.minDiff

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)  # 最小
            if self.preValue == 0x7fffffff:
                self.preValue = root.val  # 叶节点
            else:
                self.minDiff = min(self.minDiff, root.val - self.preValue)
                self.preValue = root.val
            self.inOrder(root.right)
        # me两个节题目读错，相邻节点最小
        # self.mm= 0x7fffffff
        # def  diff (node,m):
        #     if node.left:
        #         left_min=diff(node.left,m)
        #         m=min(node.val-node.left.val,m)
        #         print(left_min)
        #         print(m)
        #     if node.right:
        #         right_min=diff(node.right,m)
        #         m=min(node.right.val-node.val,m)
        #         print(right_min)
        #         print(m)

        #     self.mm=min(self.mm,m)
        #     return m

        # m=self.mm
        # diff(root,m)
        # return self.mm

        # 未来看


class Solution:
    def func(self, root, tmp):
        if root:
            tmp.append(root.val)
            tmp = self.func(root.left, tmp)
            tmp = self.func(root.right, tmp)
        return tmp

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = float('inf')
        tmp = []
        tmp = self.func(root, tmp)
        tmp.sort()
        for i in range(1, len(tmp)):
            val = tmp[i] - tmp[i - 1]
            res = min(val, res)
