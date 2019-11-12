# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         result=0
#         if not root:return 0
#         #是节点且是左节点
#         if root.left and root.left.left==None  and root.left.right==None:
#             result+= root.left.val
#         result+= self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
#         return result
#copy
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isLeaf(node):
        	if node == None:
        		return False
        	if node.left == None and node.right == None:
        		return True
        	return False

        res = 0

        if root:
        	if isLeaf(root.left):
        		res += root.left.val
        	else:
        		res += self.sumOfLeftLeaves(root.left)
        	if root.right:
        	    res += self.sumOfLeftLeaves(root.right)

        return res