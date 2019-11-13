#简单
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for m in nums:
            d[m]=d.get(m,0)+1
        a=[]
        for key,value in d.items():
            if value>n//3:
                a.append(key)
        return a