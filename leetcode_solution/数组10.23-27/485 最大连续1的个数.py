class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #1copy
        return len(max(''.join(map(str, nums)).split('0')))
    #2copy
        res, count = [], 0
        for x in nums:
            count = 0 if x == 0 else count + 1
            res.append(count)#用数组获取所有count
        return max(res)
        #muso 可以
        # count=0
        # max=0
        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         count+=1
        #         if (count>max):
        #             max=count
        #     else:
        #         count=0
        # return max