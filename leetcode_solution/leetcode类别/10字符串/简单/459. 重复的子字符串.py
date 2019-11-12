class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # copy1
        len1 = len(s)
        j = 1
        for i in range(len(s) // 2):
            a = s
            old = s[:i + 1]
            if old * (len1 // j) == s:
                return True
            j = j + 1
        return False
        # copy2更好
# i从1循环至字符串长度的一半，所有字符串长度能整除的i即代表所有可能的子字符串长度
# 判断子字符串延长给定倍数后是否等于原字符串

#         for i in range(1,len(s)//2+1):
#             if(len(s)%i==0):
#                 if s[0:i]*(len(s)//i)==s:
#                     return True
#         return False


