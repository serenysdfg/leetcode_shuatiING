class Solution:
    #未看困难
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # https://mp.weixin.qq.com/s/_yqhvJ_arayeCc0EuFO6Ow 未看
        if not nums:
            return list()

        res, stack = list(), list()
        for i, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                stack.pop()

            stack.append(i)
            if i - stack[0] >= k:
                stack.pop(0)
            if i >= k - 1:
                res.append(nums[stack[0]])

        return res