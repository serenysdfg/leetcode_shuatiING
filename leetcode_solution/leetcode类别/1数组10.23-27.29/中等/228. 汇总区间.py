#不难
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #
        if len(nums)==0:return []
        elif len(nums)==1:return [str(nums[0])]
        l=nums[0]
        a=[]
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]!=1:
                r=nums[i]   
                if l!=r:
                    a.append(str(l)+'->'+str(r))
                else:
                    a.append(str(l))
                l=nums[i+1]
        r=nums[len(nums)-1]
        if l!=r:
            a.append(str(l)+'->'+str(r))
        else:
            a.append(str(l))
        return a
