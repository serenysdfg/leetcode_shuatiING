class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        #my
#         A.sort()
#         if (len(A)==3 ): #特殊情况
#             if A[2]<A[0]+A[1]:
#                 return A[2]+A[0]+A[1]
#             else:
#                 return 0

#         for i in range(len(A)-1,1,-1):#i不会到1只到2为止
#             if A[i]<A[i-1]+A[i-2]:
#                 return A[i]+A[i-1]+A[i-2]
#         return 0
    #copy
        A.sort(reverse=True) #倒过来方便
        for i in range(len(A)-2):
            if A[i+2] + A[i+1] > A[i]:
                return A[i] + A[i+1] + A[i+2]
            
        return 0
        