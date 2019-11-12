#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 求众数
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (57.15%)
# Total Accepted:    21.3K
# Total Submissions: 37.3K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#最直观的想法, 遍历数组, 然后存储每个元素的出现次数, 如果出现次数超过 n/2,直接返回该元素即可. 时间复杂度为 O(n).
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict=dict()
        for num in nums:
            cnt=1
            if num in num_dict:
                cnt+=num_dict[num]
            if cnt>len(nums)/2:
                return num
            num_dict[num]=cnt

        
        

