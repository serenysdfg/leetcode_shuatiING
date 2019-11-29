#简单
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d={}
        for s in A:
            d[s]=d.get(s,0)+1
        for key ,value in d.items():
            if value==len(A)//2:
                return key