class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 典型DPcopy
        # 顺序乱，没有思路
        # a[i]表示以nums[i]为结尾的最长子序列长度，遍历num[i]之前的数并更新a[i]的值
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])  # 前面第几个有几个比他小的为位置+1
        print(dp)
        return max(dp)
        # copy2不是dp没看
        # mem = list()
        # len_nums = len(nums)
        # for i in range(len_nums):
        #     low, upper = 0, len(mem)
        #     while low < upper:
        #         mid = (upper - low)//2 + low
        #         if mem[mid] < nums[i]:
        #             low = mid + 1
        #         else:
        #             upper = mid

        #     if upper == len(mem):
        #         mem.append(nums[i])
        #     else:
        #         mem[upper] = nums[i]

        # return len(mem)
