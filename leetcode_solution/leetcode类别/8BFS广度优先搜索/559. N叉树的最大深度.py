# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # copy
        if not root:
            return 0
        elif not root.children:
            return 1

        return 1 + max(self.maxDepth(child) for child in root.children)  # 递归