'''给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75'''
 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #超时
        # maxSum=nums[0]
        # sum=[nums[i] for i in range(len(nums))]
        # for i in range(len(nums)-k+1):
        #     if k==1:
        #         return max(sum)
        #     for j in range(1,k):#忽视k=1
        #         sum[i]+=nums[i+j]
        #         maxSum=max(maxSum,sum[i])
        # return maxSum/k
    #copy ，用nums[0:k]
        m=f=sum(nums[0:k])
        for i in range(0,len(nums)-k):
            f+=nums[i+k]-nums[i]#加一个，减一个
            if f>m:
                m=f
        return m*1.0/k
