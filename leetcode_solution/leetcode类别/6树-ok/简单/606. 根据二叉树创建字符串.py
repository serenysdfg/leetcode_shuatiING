# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        #         res = []
        #         def dp(t):
        #             if t != None:
        #                 res.append(str(t.val))
        #                 if t.left != None:
        #                     res.append("(")
        #                     dp(t.left)
        #                     res.append(")")

        #                 if t.right != None:
        #                     if not t.left:
        #                         res.append("()")
        #                     res.append("(")
        #                     dp(t.right)
        #                     res.append(")")
        #         dp(t)

        #         return "".join(res)

        if not t: return ""
        a = []

        def dp(t):
            a.append(str(t.val))
            if t.left:
                a.append('(')
                dp(t.left)
                a.append(')')
            if t.right:
                if not t.left:  # 能省略第一个对括号来中断输入和输出之间的一对一映射关系。
                    a.append("()")
                a.append('(')
                dp(t.right)
                a.append(')')

        dp(t)
        return ''.join(i for i in a)