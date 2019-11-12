class Solution:
    def rob(self, nums: List[int]) -> int:
        #lose
        # n=len(nums)
        # sums=[nums[0] for i in range(n)]
        # for i in range(n):
        #     sums[i]=max(sums[i]+nums[i+2],sums[i]+nums[i+2])
        #copy
#         pre, cur = 0, 0
#         for i in nums:
#             pre, cur = cur, max(pre + i, cur)

#         return cur
    #copy2
        n = len(nums)
        if n ==0:
            return 0
        if n <=2:
            return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))#只会遇到2种情况，即：抢这家店和下下家店，或者不抢这家店。
        return max(dp)

