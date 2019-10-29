#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (47.05%)
# Total Accepted:    16.3K
# Total Submissions: 34.6K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 
# 说明:
# 
# 
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 
# 
# 示例:
# 
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
# 
#
#使用两个指针( head,tail)分别指向数组的首尾两个元素: 当 head<tail时:

#当 numbers[head]+numbers[tail]==target时, 返回 head+1,tail+1
#当 numbers[head]+numbers[tail]<target时, 说明头部元素需要向右移动, head=head+1
#当 numbers[head]+numbers[tail]>target时, 说明尾部元素需要向做移动, tail=tail-1
#不难得到此时的时间复杂度为 O(n)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head ,tail=0,len(numbers)-1
        while head<tail:
            now_sum =numbers[head]+numbers[tail]
            if (now_sum ==target):
                return [head+1,tail+1]
            elif(now_sum<target):
                head+=1
            else:
                tail-=1
        return None
                

