#简单0202
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return None
        res=[]
        res.append(root.val)
        if root.left:
            res.extend( self.preorderTraversal(root.left))#extend不能加none
        if root.right:
            res.extend( self.preorderTraversal(root.right))
        return res

#me2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res=[]
        self.preorder(root)
        return self.res
    def preorder(self,root):
        if not root:return []
        else:
            self.res.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
