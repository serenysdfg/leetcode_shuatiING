#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (36.68%)
# Total Accepted:    38.8K
# Total Submissions: 105.8K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。
# 
# 
#方法1: 从右其旋转k步, 其实就是将nums[-k:] 挪到前面, 将nums[:-k]挪到后面就行了

# 方法2: 一步一步地挪动, 直到挪到k步为止(然而, 这种方法超时了…)

# 方法3: 基于方法2 改进一下, 不用挪动k步, 其实一开始就能直到每个数字挪动到哪儿:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        if k >= num_len:
            k = k % num_len
        after, before = nums[:-k], nums[-k:]
        for i in range(len(before)):
            nums[i] = before[i]
        for i in range(len(after)):
            nums[i+len(before)] = after[i]
'''
    def rotateStep(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        if k >= num_len:
            k = k % num_len
        #print k
        while k > 0:
            right = nums[-1]
            tmp = nums[0]
            for i in range(1, num_len):
                now = nums[i]
                nums[i] = tmp
                tmp = now
            nums[0] = right
            k -= 1

    def rotateLess(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        if k >= num_len:
            k = k % num_len
        after = nums[:-k]
        for i in range(k):
            nums[i] = nums[num_len - k + i]
        for i in range(len(after)):
            nums[i+k] = after[i]

    def rotateSwap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        if k >= num_len:
            k = k % num_len
        def nextPos(i):
            if i >=0 and i < num_len - k:
                return i + k
            else:
                return i + k - num_len
        if k > 0:
            change_num = 0
            start_i = 0
            while change_num < num_len:
                start = nums[start_i]
                next_i = nextPos(start_i)
                while next_i != start_i:
                    # 当下一个i不等于起始i时, 继续遍历
                    tmp = nums[next_i]
                    nums[next_i] = start
                    start = tmp
                    next_i = nextPos(next_i)
                    change_num += 1
                nums[next_i] = start
                change_num += 1
                start_i += 1
'''
