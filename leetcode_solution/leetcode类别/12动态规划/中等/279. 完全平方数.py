# BFS再看没仔细看最小数
class Solution:
    dp = [0]

    # dp就是组成n所需的最小个数
    def numSquares(self, n: int) -> int:
        while len(self.dp) <= n:
            m = len(self.dp)
            inf = float('inf')
            i = 1
            while i * i <= m:  # 最多m个1,长度
                inf = min(inf, self.dp[m - i * i] + 1)  # 1 + min(dp[i - 1*1], dp[i - 2*2], dp[i - 3*3])+1
                i += 1
            print(inf)
            self.dp.append(inf)  # 1,2 ,3,4
        return self.dp[n]
        # q = list()#广度优先
        # q.append([n, 0])# 创建队列
        # visited = [False for _ in range(n + 1)]
        # visited[n] = True# 保存遍历过的结点
        # # 遍历队列里的节点
        # while any(q):
        #     num, step = q.pop(0) #174  0

        #     i = 1
        #     tnum = num - i ** 2 #17-1
        #     while tnum >= 0:
        #         # 最先到达0的一定是步数最少的
        #         if tnum == 0:
        #             return step + 1
        #         # 只添加没有遍历过的节点
        #         if not visited[tnum]:
        #             q.append((tnum, step + 1))#（16，1） （7，1 ，（0，1#可能的情况-4  -9  -16
        #             visited[tnum] = True
        #         i += 1
        #         tnum = num - i ** 2 #16-4 16-9  16-16

        # copy2四平方定理
        # while n % 4 == 0:
        #     n /= 4

        # if n % 8 == 7:
        #     return 4

        # a = 0
        # while a**2 <= n:
        #     b = int((n - a**2)**0.5)
        #     if a**2 + b**2 == n:
        #         return (not not a) + (not not b)

        #     a += 1

        # return 3

# copy没看1https://blog.csdn.net/qq_17550379/article/details/80875782
# q = list()
# q.append([n, 0])
# visited = [False for _ in range(n+1)]
# visited[n] = True

# while any(q):
#     num, step = q.pop(0)

#     i = 1
#     tNum = num - i**2
#     while tNum >= 0:
#         if tNum == 0:
#             return step + 1

#         if not visited[tNum]:
#             q.append((tNum, step + 1))
#             visited[tNum] = True

#         i += 1
#         tNum = num - i**2

# 失败回溯？
# 先找最相近的   sqrt
# 找平方根？3-4之间，减去后再继续？ 9+3 不行4*3
# print(n)
# if n==1:return 1
# if n==0:return 0
# count=0
# for i in range(n//2):#4开始
#     if i*i==n:return 1
#     elif i*i>n:
#         count+=1 #1  sel(4) 2:
#         # print(count)
#         count+=self.numSquares(n-(i-1)*(i-1))
# return count