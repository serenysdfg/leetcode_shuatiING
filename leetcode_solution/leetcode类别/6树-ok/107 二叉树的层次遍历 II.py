# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#未看
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # copy
        res = []

        if root == None: return []

        curLevel = [root]
        while curLevel:
            nextLevel = []
            tmpRes = []
            for node in curLevel:
                tmpRes.append(node.val)
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            res.append(tmpRes)
            curLevel = nextLevel
        res.reverse()
        return res