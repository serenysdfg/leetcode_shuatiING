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
'''
解题思路

使用一个二维数组维护从i到j的子数组之和, 遍历数组, 每次遍历数组需要更新第i列的值, 遇到sum大于等于s的, 可以判断其与当前最小长度的大小比较, 并基于此进行更新.

然后…超过内存限制了. 其实在更新二维数组的过程中, 我们不难发现: 有很多数组是肯定没有用的, 那么我们可以考虑只存储一个一维数组用来记录即可, 因为其实之前的数组都已经没用了

然后…超过时间限制了. 想想有木有O(nlogn)的方法, 考虑还是使用一个数组用来记录从0到i的和, 那么每次只需要使用二分进行查找s+nums[i]的值. 然后这样的话就不用每次都去更新sum的值了, 最后时间复杂度O(nlogn)即可.

参考了一下资料, 找到一种O(n)的方法, 使用两个指针, 分别记录当前子数组的前后索引, 然后sum存储当前子序列的和, 什么时候更新子序列呢? 当sum < s的时候, 右指针继续向右移动, sum增加; 当sum >=s时, 左指针向右移动, 根据情况进行更新最后的值.
'''
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums) #暴力法
        min_num = 0
        sums = [[0 for _ in range(num_len)] for _ in range(num_len)]  #n*n
        for i in range(num_len):
            num = nums[i]
            for j in range(i+1):
                if i >= 1:
                    sums[i][j] = sums[i-1][j] + num
                else:
                    sums[i][j] = num
                if sums[i][j] >= s and (min_num == 0 or i-j+1 <= min_num):
                    min_num = i - j + 1
        return min_num

    def minSubArrayLenI(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        min_num = 0
        sums = [0 for _ in range(num_len)]
        for i in range(num_len):
            num = nums[i]
            for j in range(i+1):
                if sums[j] < s:
                    sums[j] += num
                    if sums[j] >= s and (min_num == 0 or i-j+1 <= min_num):
                        min_num = i - j + 1
        return min_num

    def minSubArrayLenII(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(nums, s, left, right):
            #二分查找, 找到大于s的数字的最小下标,如果没有,返回0
            if right >= len(nums) or left >= len(nums):
                return -1
            if nums[left] >= s:
                return left
            mid = (left + right) // 2
            if nums[mid] > s:
                return binarySearch(nums, s, left, mid)
            elif nums[mid] < s:
                return binarySearch(nums, s, mid + 1, right)
            else:
                return mid
        min_num = 0
        num_len = len(nums)
        sums = [nums[i] for i in range(num_len)]
        for i in range(1, num_len):
            sums[i] = sums[i-1] + nums[i]
        # [2,3,1,2,4,3] 得到 [2,5,6,8,12,15], 接下来使用二分查找
        for i in range(num_len):
            num = nums[i]
            index = binarySearch(sums, s, i, num_len-1)
            new_index = index + 1 - i
            if index >= 0 and (min_num == 0 or new_index <= min_num):
                min_num = new_index
            s += num
        return min_num

    def minSubArrayLenIII(self, s, nums):
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
'''
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
        

