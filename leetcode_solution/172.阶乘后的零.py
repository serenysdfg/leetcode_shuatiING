#
# @lc app=leetcode.cn id=172 lang=python
#
# [172] 阶乘后的零
#
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (36.92%)
# Total Accepted:    8K
# Total Submissions: 21.5K
# Testcase Example:  '3'
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
# 
# 示例 1:
# 
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 
# 示例 2:
# 
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 
# 说明: 你算法的时间复杂度应为 O(log n) 。
# 
#        
# 所以最后只需要统计 2和 5的个数即可. 现了 5必定会出现 2, 因此只需要统计出现 5的次数即可. 例如 28中出现了 25, 20, 15, 10, 5, 其中 25=5*5, 应该要算 2个.
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>0:
            count+=n/5
            n/=5
        return count

