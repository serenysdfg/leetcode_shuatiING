# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         result = list()
#         if root == None:
#             return result
#         if root.left == None and root.right == None:
#             result.append(str(root.val))
#             return result
#         left = self.binaryTreePaths(root.left)
#         for i in range(len(left)):
#             result.append(str(root.val) + '->' + left[i])

#         right = self.binaryTreePaths(root.right)
#         for i in range(len(right)):
#             result.append(str(root.val) + '->' + right[i])

#         return result

#     #copy2
#     递归+DFS
class Solution(object):
    def binaryTreePaths(self, root):
        def helper(node, cur_path):
            if not node.left and not node.right:  ## 到leaf了
                res.append(cur_path + [node.val])
                return
            if node.left:
                helper(node.left, cur_path + [node.val])
            if node.right:
                helper(node.right, cur_path + [node.val])

        res = []
        if not root: return res
        helper(root, [])
        return ['->'.join([str(val) for val in path]) for path in res]  # res存储很多path