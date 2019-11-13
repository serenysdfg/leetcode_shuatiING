# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #递归，copy
    # 左右侧查找的结果都不为空，说明分别找到了p和q。祖先可以是节点自己。然后根据左右侧找到的节点做进一步的判断。
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #copy
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)#在同一个子树上p，q。p == root or q == root
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:#不在同一个子树left and right
            return root
        return left if left else right


