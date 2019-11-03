给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

 

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #双指针-未看
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1
        #
        # def afterChange(s): 
        #     res = ''
        #     for i in s:
        #         if i == '#':
        #             res = '' if len(res) == 0 else res[:-1]#不能再往前如果没有字符。。res[:-1]:去掉最后一个
        #         else:
        #             res += i
        #     return res
        # return afterChange(S) == afterChange(T)
        #花费很久,很多没考虑
#         S=list(S)
#         T=list(T)
#         s=[]
#         t=[]
#         for i in range(len(S)):
#             if S[i]=='#':  #刚开始如果是#
#                 i+=1
#             else:
#                 break                
#         for j in range(len(T)):
#             if T[j]=='#':  #刚开始如果是#
#                 j+=1
#             else:
#                 break
                            
#         for i in range(i,len(S)):#从i开始

#             if S[i]!='#':
#                 s.append(S[i])
#             elif len(s)>0 :#不能为0
#                 s.pop()
#         for j in range(j,len(T)):

#             if T[j]!='#':
#                 t.append(T[j])
#             elif len(t)>0 :
#                 t.pop()
#         if len(t)!=len(s):return False:#最后多出的部分..直接s==t比较就可以
#         for k in range(len(t)):
#             if s[k]!=t[k]:
#                 return False
#         return True