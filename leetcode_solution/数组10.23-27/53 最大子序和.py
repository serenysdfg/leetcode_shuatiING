class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    #动态规划,copy 只关注：当然值 和 当前值+过去的状态，是变好还是变坏;到i处的最大值两个可能，一个是加上a[i], 另一个从a[i]起头
#         n = len(nums)
#         maxSum = [nums[0] for i in range(n)]
#         for i in range(1,n):
#         	maxSum[i] = max(maxSum[i-1] + nums[i], nums[i])
#         return max(maxSum)
#     #copy:,两个nums[0],选择更新后更大的
#         n = len(nums)
#         maxSum , maxEnd = nums[0], nums[0]
        
#         for i in range(1,n):
#         	maxEnd = max(nums[i],maxEnd + nums[i])
#         	maxSum = max(maxEnd,maxSum)
#         return maxSum
    #分治法copy
        n = len(nums)
        if n == 1:#递归终止条件
            return nums[0]
        else:            
            max_left = self.maxSubArray(nums[0:len(nums) // 2])#递归计算左半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])#递归计算右半边最大子序和
        
        #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r)

