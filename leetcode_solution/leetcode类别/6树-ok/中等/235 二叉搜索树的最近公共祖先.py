# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:return root#不是返回none其他两种情况
        elif p.val < root.val < q.val or q.val < root.val < p.val :
            return root
        elif p.val < root.val and q.val < root.val: #在左边继续找
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)



#一样

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #如果有更深的，一定在同一边
        if root==p or root==q or not root or  p.val<root.val<q.val or p.val>root.val>q.val :return root
        elif p.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q) #要用return
        elif p.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)