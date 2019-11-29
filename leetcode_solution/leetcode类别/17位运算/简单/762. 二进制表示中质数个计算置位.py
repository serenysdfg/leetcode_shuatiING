class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        one_list = [2, 3, 5, 7, 11, 13, 17, 19] #有范围方便,注审题在 [1, 10^6] 中的整数
        for a in range(L, R + 1):
            if bin(a).count('1') in one_list:
                count += 1
        return count