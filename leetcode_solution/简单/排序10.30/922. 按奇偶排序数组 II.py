class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B=[]
        C=[]
        D=[]
        for i in range(len(A)):
            if A[i]%2==0:
                B.append(A[i]) #偶数
            else:
                C.append(A[i])
        for i in range(len(B)):
            D.append(B[i]) #添加偶数
            D.append(C[i])# 添加奇数
        return D
    #copy
        A_len, i, j = len(A), 0, 1
        result = [0]*A_len
        for a in A:
            if a&1 == 0:
                result[i] = a #先定义数组。隔两个赋值
                i += 2
            else:
                result[j] = a
                j += 2

        return result