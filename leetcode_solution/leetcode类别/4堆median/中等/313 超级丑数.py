class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 3copy
        dp = [1] #dp[0]=1
 
        lenPrimes = len(primes)
        idxPrimes = [0] * lenPrimes
        counter = 1
        while counter < n:
            min = pow(2, 32)
            for i in range(0, lenPrimes):
                temp = dp[idxPrimes[i]] * primes[i] #获取最小值
                if temp < min:
                    min = temp
 
            for i in range(0, lenPrimes):
                if min == dp[idxPrimes[i]] * primes[i]:
                    idxPrimes[i] += 1#找到对应的最小值
            dp.append(min)
            counter += 1
 
        return dp[counter - 1]