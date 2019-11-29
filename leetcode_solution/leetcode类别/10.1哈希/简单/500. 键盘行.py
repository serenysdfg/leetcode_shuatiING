class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #me
        # d=['qwertyuiop','asdfghjkl','zxcvbnm']
        # result=[]
        # for word in words:
        #     w=word.lower() 
        #     for i in range(len(d)):
        #         if w[0] in d[i]:
        #             flag=1 #在同一行
        #             for j in range(1,len(w)):
        #                 if w[j] not in  d[i]:
        #                     flag=0
        #                     break
        #             if flag:result.append(word)
        #             break
        # print(result)
        # return result


        ans=[]
        keyset=['qwertyuiop','asdfghjkl','zxcvbnm']
        for keys in keyset:
            for word in words:
                line=set(word.lower())
                if line.issubset(set(keys)):
                    ans.append(word)
        return ans
