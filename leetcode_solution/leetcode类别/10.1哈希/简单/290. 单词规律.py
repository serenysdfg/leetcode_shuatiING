class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        #和205类似
        #注意前后都可能两个对应一个
        strlist=str.split(' ')
        if len(strlist) != len(pattern): return False
        return len(set(strlist)) == len(set(pattern)) == len(set(zip(strlist, pattern)))
        #me
    #     strlist=str.split(' ')
    #     return self.iso(strlist,pattern) and self.iso(pattern,strlist) #反过来
    # def iso(self,pattern,strlist):
    #     if len(pattern)!=len(strlist):return False
    #     d={}
    #     for i in range(len(strlist)):
    #         if pattern[i] not in d:
    #             d[pattern[i]]=strlist[i]
    #         else:
    #             if d[pattern[i]]!=strlist[i]:
    #                 return False
    #     return True