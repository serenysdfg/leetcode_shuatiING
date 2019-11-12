class Solution:#好题
    def buddyStrings(self, A: str, B: str) -> bool:
        #1长度不等不可以 2不同标记
        if len(A) != len(B):
            return False
        if A ==B: #相等
            q =set(A)
            for i in q:
                if A.count(i) >=2:
                    return True
            return False
        dic = zip(A,B)
        dic = dict(dic)
        flag = 0
        a_list =[]
        b_list =[]
        for i,j in dic.items():
            if i != j:
                flag +=1
                a_list.append(i)
                b_list.append(j)
        if flag == 2 and a_list == b_list[::-1]:#两个h换过来
            return True
        else:
            return False

# class Solution:#失败还有其他的不同没考虑
#     def buddyStrings(self, A: str, B: str) -> bool:        
#         if(len(A)!=len(B)):
#             return False
#         k=0
#         for i in range(len(A)):
#             if A.count(A[i]) >=2:
#                 return True
#             if(A[i]!=B[i]): 
#                 k=i
#                 break
#             #全都相等没有超过2个的
#             return False #不会中断
#         for i in range(k+1,len(A)):
#             if(A[i]!=B[i]):
#                 if A[i]==B[k] and B[i]==A[k]:
#                     return True
#                 else:
#                     return False
