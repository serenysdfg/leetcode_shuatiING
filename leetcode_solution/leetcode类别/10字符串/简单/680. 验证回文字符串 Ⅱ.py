class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 解题思路：
        # 从字符串两端向中间进行判断，当两个字母不等时，跳出循环
        # 将字符串改为当前指针的位置，分别判断改变后的字符串从左端、右端减去一个后，是否与其反转后的字符串相等（回文串），若有一个相等即满足条件

        # l,r=0,len(s)-1
        # flag=0#未删除字符
        # while l<r:
        #     if s[l]!=s[r]:
        #         flag=1
        #         break
        #     l+=1
        #     r-=1
        # if flag==0:return True
        # s=s[l:r+1]
        # return s[:-1]==s[:-1][::-1] or s[1:]==s[1:][::-1]

        r = s[::-1]
        if s == r:
            return True
        for i in range(len(s)):
            if s[i] != r[i]:
                m = s[:i] + s[i + 1:]  # 去掉i
                if m != m[::-1]:
                    n = r[:i] + r[i + 1:]
                    return n == n[::-1]
                else:
                    return True

        # 从字符串的左右两端同时开始遍历比较，去除不相同的那个字母（左边或者右边的）后再进行判断。

#         for i in range(len(s)//2):
#             if s[i] !=  s[len(s)-i-1]:
#                 s=s.replace(s[i],'')
