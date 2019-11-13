给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例
1:

输入: [1, 2, 3]
输出: 6
示例



class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
#         最大乘积有三种情况：
# （1）当数组中全是正数时，最大乘积为第一大数X第二大数X第三大数
# （2）当数组中全是负数时，最大乘积为第一大数X第二大数X第三大数 -6 -5 -4 -3 -2 -1
# （3）当数组中正负数都有时，最大乘积为第一大数X第二大数X第三大数（两个正数），
# 或者第一大数X第一小数X第二小数（一个正数），取两者之中的最大值。
        #注意负数
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        l = max(nums)
        nums.remove(l)
        m = max(nums)
        j = min(nums)
        nums.remove(m)
        nums.remove(j)
        n = max(nums)
        k = min(nums)
        sum = max(l*m*n, l*j*k)
        return sum
