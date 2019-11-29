class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #考虑不全
        #copy2未看
        # if n == 1:
        #     return 1
        # else:
        #     import collections
        #     q2 = collections.deque()
        #     q3 = collections.deque()
        #     q5 = collections.deque()
        #     q2.append(2)
        #     q3.append(3)
        #     q5.append(5)
        #     while n > 1:
        #             x = min(q2[0],q3[0],q5[0])
        #             if x == q2[0]:
        #                     x = q2.popleft()
        #                     q2.append(2*x)
        #                     q3.append(3*x)
        #                     q5.append(5*x)
        #             elif x == q3[0]:
        #                     x = q3.popleft()
        #                     q3.append(3*x)
        #                     q5.append(5*x)
        #             else:
        #                     x = q5.popleft()
        #                     q5.append(5*x)
        #             n -= 1
        #     return x
        #copy
        res = [1]
        in1 = 0
        in2 = 0
        in3 = 0
        for i in range(n-1):
            res.append(min(res[in1]*2,res[in2]*3,res[in3]*5)) #里面的数字相乘ins是序号  2    
            if res[-1] == res[in1] * 2: #加了2.下次res[ins1]=2
                in1 += 1
            if res[-1] == res[in2] * 3:#下次res[ins2]=2   1*3   2*3  3*3  4*3 5*3添加的数字*3只能是里面的数字
                in2 += 1
            if res[-1] == res[in3] * 5:
                in3 += 1
        return res[-1]
        # #循环计数？东归  dp[i]= 有错
        # dp=[0 for _ in range(n)]
        # dp[0]=1
        # m=1
        # k=1
        # p=1
        # for i in range(1,n):
        #     dp[i]=min(m*2,k*3,p*5)
        #     if m*2==dp[i]: m+=1 #切不能有其他的mkp只能是2.3.5的倍数
        #     if k*3==dp[i]: k+=1
        #     if p*5==dp[i]: p+=1
        #     print(dp[i])

        # return dp[n-1]