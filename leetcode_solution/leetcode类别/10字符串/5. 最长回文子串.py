#m没看中等https://github.com/apachecn/Interview/blob/master/docs/Algorithm/Leetcode/Python/005._longest_palindromic_substring.ipynb
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         #回文，copy
#         #最笨的方法，就是依次把每一个字符当做回文字符串的中间的那个字符，向两边扩展
#         n = len(s)

#         m,l,r = 0,0,0

#         for i in range(n):
#             # odd case
#             for j in range(min(i+1,n-i)):
#                 if s[i-j] != s[i+j]:
#                     break
#                 if 2*j + 1 > m :
#                     m = 2 * j + 1
#                     l = i-j
#                     r = i+j


#             if i+1 < n and s[i] == s[i+1]:
#                 for j in range(min(i+1,n-i-1)):
#                     if s[i-j] != s[i+j+1]:
#                         break
#                     if 2 * j + 2 > m :
#                         m = 2*j +2
#                         l = i-j
#                         r = i+j+1


#        return s[l:r+1]
    #copy联想我们之前做的动态规划的问题，也就是 72 题，思想是一样的，但是更简单
    # 一个比较好的想法是 s 和 reverse(s) 共有的最长的 substring 就是 longest palindromic substring：回文，反过来相同
    #但是bug求出来的substring indices是 0:2 但是这个s1[0:2] 和 s2[0:2]一样，所以不行 ABXYBA   ABYXBA
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def lcs(s1, s2):
            m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
            longest, x_longest = 0, 0
            for x in range(1, 1 + len(s1)):
                for y in range(1, 1 + len(s2)):
                    if s1[x - 1] == s2[y - 1]:
                        m[x][y] = m[x - 1][y - 1] + 1
                        if m[x][y] > longest:
                            longest = m[x][y]
                            x_longest = x
                    else:
                        m[x][y] = 0
            return s1[x_longest - longest: x_longest]

        return lcs(s, s[::-1])