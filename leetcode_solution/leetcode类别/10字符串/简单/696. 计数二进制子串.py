class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 太复杂，失败
        # n=len(s)
        # count=0
        # for i in range(n-1):
        #     j=i
        #     dict={}
        #     while j<n-2:
        #         if s[j]==s[j+1]:
        #             dict[s[j]]=dict.get(s[j],0)+1
        #             j+=1
        #         j+=1
        #         while s[j]==s[j+1]:
        #             dict[s[j]]=dict.get(s[j],0)+1
        #             j+=1
        #         if  dict['0']== dict['1']:
        #             count+=1
        # return count
        # copy

        pre, cur, res = 0, 1, 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1  # 交界处
            else:
                res += min(pre, cur)  # res=0
                pre, cur = cur, 1  # 交换，此时pre是前面的个数，cur重新计算

        return res + min(pre, cur)
    # 反思 01有一个，0011就有两个000111就有三个，遍历字符串，当第i个字符和第i-1个字符一样时，cur++
# 反之，是0和1的交界处，计算pre和cur中更小的值，为有效子串的个数，有多长就有多少个，再将cur赋值给pre


