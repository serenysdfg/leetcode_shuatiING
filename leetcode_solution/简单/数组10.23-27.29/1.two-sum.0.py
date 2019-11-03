#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (44.43%)
# Total Accepted:    240.8K
# Total Submissions: 542K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #新建立一个空字典用来保存数值及其在列表中对应的索引
        dict1 = {}
	    #遍历一遍列表对应的时间复杂度为O(n)
        for i in range(0, len(nums)):
            #相减得到另一个数值
            num = target - nums[i]
            #如果另一个数值不在字典中，则将第一个数值及其的索引报错在字典中
            #因为在字典中查找的时间复杂度为O(1)，因此总时间复杂度为O(n) 
            if num not in dict1:
                dict1[nums[i]] = i
            #如果在字典中则返回
            else:
                return [dict1[num], i]
        
