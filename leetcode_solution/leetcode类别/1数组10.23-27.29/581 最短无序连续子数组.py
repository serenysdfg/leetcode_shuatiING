'''给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例
1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对[6, 4, 8, 10, 9]
进行升序排序，那么整个表都会变为升序排序。
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #me超时
        # a,b=nums,nums
        # count1,count2=0, 0
        # while len(a)>0:
        #     while a[0]==min(a):
        #         a=a[1:]
        #         count1+=1
        #         if count1==len(nums):
        #             return 0
        # while len(b)>0:
        #     while b[len(b)-1]==max(b):
        #         b=b[:-1]
        #         count2+=1
        # return len(nums)-count1-count2
    #copy
        t = sorted(nums)#赋值一份先排序再比较
        n = len(nums)
        left, right, = 0, n-1
        while left<n:
            if t[left] != nums[left]:
                break
            left += 1
        if left == n:
            return 0
        while right>0:
            if t[right] != nums[right]:
                return right - left +1
            right -= 1
        return right-left+1