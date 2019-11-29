class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]: #找到重复出现的整数，再找到丢失的整
    #me题意不一定按照顺序
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1 #d[1]=1 d[2]=2 d[3]=3 d[4]=2
        for i in range(len(nums)):
            if d[nums[i]]==2:
                a=nums[i]
            if i+1 not in d.keys():
                b=i+1
        return [a,b]