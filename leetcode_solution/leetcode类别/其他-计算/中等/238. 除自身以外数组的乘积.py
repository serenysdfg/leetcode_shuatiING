class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #utput[i] =  { i 前面的数的乘积}  X  { i 后面的数的乘积}
        #copy2标准
        '''我们不用数组来存储相关的 R了, 只使用一个变量来存储右边元素的的乘积, 然后不断更新 output[i]=output[i]*right. 对于给定的索引 i, output[i]包含所有左边数字的乘积, 然后 right包含所有右边元素的乘积, 然后 R=R*nums[i].'''
            # if nums == [] : return []
            # size = len(nums)
            # output = [1] * size
            # left = 1
            # for x in range(size-1):
            #     left *= nums[x]
            #     output[x+1] *= left
            # right = 1
            # for x in range(size - 1, 0, -1):
            #     right *= nums[x]
            #     output[x-1] *= right
            # return output
        #copy
            if nums == [] : return []
            lft = [1]
            rgt = [1]
            product = 1
            for i in range(1,len(nums)):
                product *= nums[i-1]
                lft.append(product)
            product = 1
            for i in reversed(range(1,len(nums))):
                product *= nums[i]
                rgt.append(product)
            rgt.reverse()
            result = []
            for i in range(len(nums)):
                result.append(lft[i]*rgt[i])
            return result