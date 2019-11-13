class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #copy内存消耗太大
#         if s == '': return True
#         for i in range(len(t)):
#         	if t[i] == s[0]:
#         		return self.isSubsequence(s[1:],t[i+1:]) #递归

#         return False
    
        if s == '': return True
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps >= len(s)