给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字
x
的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 - 1。


输入: [1, 2, 1]
输出: [2, -1, 2]



class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # dic,stack={},[]
        # for n in nums:
        #     while stack and  stack[-1]<n:
        #         dic[]

        # copy循环,未看
        stack, nums_len = list(), len(nums)
        res = [-1] * nums_len
        for i in range(nums_len * 2):
            while stack and nums[stack[-1]] < nums[i % nums_len]:
                res[stack.pop()] = nums[i % nums_len]
            stack.append(i % nums_len)

        return res