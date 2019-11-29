class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #copy
        # if len(s) != len(t): return False
        # return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        #2
    #     return self.iso(s,t) and self.iso(t,s) #反过来
    # def iso(self,s, t):
    #     mapx = {}
    #     for i in range(len(s)):
    #         if s[i] not in mapx:
    #             mapx[s[i]] = t[i]
    #         elif s[i] in mapx:
    #             if t[i] != mapx[s[i]]:
    #                 return False
    #     return True
        #3copy
        dic = {}
        j = 0
        for i in s:
            if i not in dic.keys() and t[j] not in dic.values():
                dic[i]=t[j]
            elif (i in dic.keys() and dic[i] != t[j]) or (i not in dic.keys() and t[j] in dic.values()):
                return False
            j = j+1
        return True

            #不完整me
        # if len(s)!=len(t):return False
        # d={}
        # for i in range(len(t)):
        #     if s[i] not in d:
        #         d[s[i]]=t[i]
        #     else:
        #         if d[s[i]]!=t[i]:
        #             return False
        # return True

