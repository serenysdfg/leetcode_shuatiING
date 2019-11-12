# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #copy
# 因为根节点要在数据序列的中间，所以使用二分查找选择根节点。还有既然是高度平衡，构建树的同时，一定要均衡，所以把比中间值小的部分用于构建左子树，把比中间值大的部分，用于构建右子树
        if not nums:
            return None
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root