class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        #反转后就是前后交换，先获取再记录很麻烦
        # S=list(S)
        # i=0
        # j=len(S)-1
        # while i<j:
        #     while not S[i].isalpha() and i<len(S)-1:
        #         i+=1
        #         print(i)
        #     while not S[j].isalpha() and j>0:
        #         j-=1
        #     if i<j:
        #         S[i],S[j]=S[j],S[i]
        #         i+=1
        #         j-=1
        # return ''.join(i for i in S)
        #copy反转后对比，反过来后，判断是不是字母，是字母就赋值给S，不是字母S不变
        S = list(S)
        q = S[::-1]
        j = 0
        i = 0
        while i < len(S) and j <len(S):
            if 'a' <= q[j] <= 'z' or 'A' <= q[j] <= 'Z':
                if 'a' <= S[i] <= 'z' or 'A' <= S[i] <= 'Z':
                    S[i] = q[j]
                    i += 1
                    j +=1
                else: #到和有字幕的比较，把字母的赋值，反过来
                    i +=1
            else:
                j +=1
        return ''.join(S)
