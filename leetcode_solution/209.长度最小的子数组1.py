#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (37.54%)
# Total Accepted:    8.1K
# Total Submissions: 21.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
# 
# 示例: 
# 
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 
# 
# 进阶:
# 
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        now_sum = 0
        left = 0
        ans = 0
        for i in range(len(nums)):
            now_sum += nums[i]
            while now_sum >= s:
                now_sum -= nums[left]
                step = i - left + 1
                if ans == 0 or step <= ans:
                    ans = step
                left += 1
        return ans
        

