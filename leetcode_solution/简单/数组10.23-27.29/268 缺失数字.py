class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1copy1
        return int(len(nums) * (len(nums) + 1) / 2 - sum(nums)) #(n=9,长度也是9)等差数列前n项和减去数组之和,一行瞬秒 ，len(nums)就是max（num）
        ## my su:错误 输入0.1.2等的时候u错误
        # if max(nums)==0:
        #     return 1
        # nums.sort()
        # for i in range(max(nums)):
        #     if i not in nums:
        #         return i