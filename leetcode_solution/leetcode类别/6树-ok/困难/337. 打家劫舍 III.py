
'''在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
''''

'''从root开始抢起来，最大能抢到的两个可能： 抢root和不抢root

rob_root = max(rob_L + rob_R , no_rob_L + no_nob_R + root.val)
no_rob_root = rob_L + rob_R
对于每个node，我们return的是从这个node能抢到的最大值，以及不抢它能获得的最大值，这个递归简直我服


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  # copy
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root: return 0, 0
            rob_L, no_rob_L = dfs(root.left) #抢，不抢
            rob_R, no_rob_R = dfs(root.right)
            return max(no_rob_R + no_rob_L + root.val, rob_L + rob_R), rob_L + rob_R

        return dfs(root)[0]

'''###2'''

class Solution:#copy
    def rob(self, root: TreeNode) -> int:
        check = self.rob1(root)
        return max(check[0], check[1])

    def rob1(self, root):
        if not root:
            return [0, 0]

        l, r = self.rob1(root.left), self.rob1(root.right)
        return l[1] + r[1] + root.val, max(l) + max(r)
