'''给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#中序遍历
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res=[]
        def dp(root):
            if root!=None:
                dp(root.left)
                res.append(root.val)
                dp(root.right)
        dp(root)
        res=list(set(res))
        res.sort()
        return res[1] if len(res)>1 else -1