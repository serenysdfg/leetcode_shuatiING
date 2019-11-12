class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        #选择负数最小,mysolution
        # A.sort()
        # for i in range(K):
        #     if A[i]<0:
        #         A[i]*=(-1)
        #     else:#要重新排序，可能已经变成正数的更小
        #         A.sort()
        #         A[0]*=(-1)
        # return sum(A)
        #copy
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i)%2*min(A)*2 #利用了min方法，全部加起来后再减去