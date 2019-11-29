class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #1+
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]math.factorial(n-1)
            rest = nums[:i] + nums[i+1:]#第一个不变--第二个不变
            for j in self.permuteUnique(rest):
                if [prefix]+j not in res: #多加一句
                    res.append([prefix]+j)
        return res

