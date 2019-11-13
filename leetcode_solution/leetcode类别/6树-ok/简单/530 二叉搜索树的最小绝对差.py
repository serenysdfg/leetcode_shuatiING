# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 任意两节点不是相邻节点，注意审题，开始写错
        #         a=[]
        #         stack = [root]

        #         while stack:
        #             node = stack.pop()
        #             print (node.val)
        #             print( node.left)
        #             if node.left: #要判断是否存在节点
        #                 a.append(node.left.val)
        #                 stack.append(node.left)
        #             if node.right:
        #                 a.append(node.right.val)
        #                 stack.append(node.right)
        #         # print (a)
        #         return sorted(a)[0]

        # copy
        result = sys.maxsize  ##9223372036854775807
        l = []
        pre = None
        while root or l:
            if (root):
                l.append(root)
                root = root.left
            else:
                node = l.pop()
                if (pre != None):
                    result = min(node.val - pre, result)
                pre = node.val
                root = node.right
        return result


