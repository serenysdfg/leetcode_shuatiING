# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         #超时
#         if root==None:return None
#         a=[]
#         while root:
#             if root.left:
#                 self.increasingBST(root.left)
#             a.append(root)
#             if root.right:
#                 self.increasingBST(root.right)
#         print(a)
#         return a
# copy未看
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(-1)
        self.prev = dummy
        self.inOrder(root)
        return dummy.right

    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        root.left = None
        self.prev.right = root
        self.prev = self.prev.right
        self.inOrder(root.right)
