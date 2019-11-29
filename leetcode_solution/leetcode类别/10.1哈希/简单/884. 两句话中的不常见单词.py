#ME

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d={}
        a=[]
        A=A.split(' ')
        B=B.split(' ')
        for s in A:
            d[s]=d.get(s,0)+1
        for s in B:
            d[s]=d.get(s,0)+1
        for key,value in d.items():
            if value==1:
                a.append(key)
        return a