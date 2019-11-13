# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # copy
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,
                                                                                          q.right)  # 递归左右节点，内容相同

        if p == None and q == None:  # 空
            return True
        else:
            return False
#copy2
        return p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) if p and q else p is q
#xopy3
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False