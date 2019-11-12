# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        for key in  list(dict.keys()):
            if dict[key]==1:
                return key
            #copy位运算
        # num = nums[0]
        # for i in range(1, len(nums)):
        #     num = num ^ nums[i] #两次异或后就会变为0，一次就是那个数字
        #
        # return num
