# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #copy
    def findMode(self, root):
        if root is None:
            return []
        dict_tree = {root.val:1}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: #一个个节点遍历值。先放进栈中
                if node.left.val in dict_tree:
                    dict_tree[node.left.val] += 1
                else:
                    dict_tree[node.left.val] = 1
                stack.append(node.left)
            if node.right:
                if node.right.val in dict_tree:
                    dict_tree[node.right.val] += 1
                else:
                    dict_tree[node.right.val] = 1
                stack.append(node.right)

        maxnum = sorted(dict_tree.values())[-1]#字典排序
        return [i for i in dict_tree if dict_tree[i] == maxnum]