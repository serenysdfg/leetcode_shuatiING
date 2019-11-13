#中序

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#简单
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # #左跟右，中序遍历
        # res=[]
        # def dp(root):
        #     if root!=None:
        #         dp(root.left)
        #         res.append(root.val)
        #         dp(root.right)
        # dp(root)
        # res=list(set(res))
        # res.sort()
        # return res[k-1]
    #迭代
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if not k: #k=0
                return root.val
            root=root.right