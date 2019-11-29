# Definition for a binary tree node
#有难度：二叉树+dp
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''不同的数作为root，会产生什么样的结果呢？这就由i左边的数可以构成什么样的二叉搜索树，i右边的数可以构成什么样的二叉搜索树决定。接着我们就会在i的左边去找一个左子树root，在i的右边去找一个右子树的root，这就是递归的过程。右边的树值大左边小'''
        if n == 0:
            return list()

        mem = dict()
        return self._generateTrees(1, n, mem)

    def _generateTrees(self, left, right, mem):
        if left > right:  # 只剩一个的时候i为最左边计算左节点i=left或者right返回null
            return [None]
        if (left, right) in mem:
            return mem[(left, right)]

        res = list()
        for i in range(left, right + 1):
            left_nodes = self._generateTrees(left, i - 1, mem)  # i为跟节点
            right_nodes = self._generateTrees(i + 1, right, mem)
            for left_node in left_nodes:  # 返回的res是list
                for right_node in right_nodes:
            root = TreeNode(i)  # 建立节点
            root.left = left_node
            root.right = right_node
            res.append(root)

        mem[(left, right)] = res  # 用于记忆，不用重复构造
        return res
