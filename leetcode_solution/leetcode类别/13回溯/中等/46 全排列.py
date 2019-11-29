'''给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #copy
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i+1:]#第一个不变--第二个不变
            for j in self.permute(rest):
                res.append([prefix]+j)
        return res