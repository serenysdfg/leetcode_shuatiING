class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps={}
        for i in s:
            maps[i]=maps.get(i,0)+1
        for x,c in enumerate(s):
        	if maps[c] == 1:
        		return x
        return -1

#copy
        # q = list(set(s))
        # lis = []
        # for i in range(len(q)):
        #     if s.count(q[i]) == 1:
        #         lis.append(s.index(q[i]))
        # if lis:
        #     return min(lis)
        # else:
        #     return -1
