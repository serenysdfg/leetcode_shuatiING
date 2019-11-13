class Solution:
    def fib(self, N: int) -> int:
        
        if N==0: return 0
        pre = 1
        ppre = 0
        for i in range(1,N):
            pre,ppre =  pre+ppre,pre
        return pre
    #不行so
#         if (N==0):
#             return 0
#         if (N==1):
#             return 1
#         return fib(N - 1) + fib(N - 2);
    
