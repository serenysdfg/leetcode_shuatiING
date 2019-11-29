#BFS再看没仔细看最小数
class Solution:
    def numSquares(self, n: int) -> int:

        q = list()#广度优先
        q.append([n, 0])# 创建队列
        visited = [False for _ in range(n + 1)]
        visited[n] = True# 保存遍历过的结点
        # 遍历队列里的节点
        while any(q):
            num, step = q.pop(0) #174  0

            i = 1
            tnum = num - i ** 2 #17-1
            while tnum >= 0:
                # 最先到达0的一定是步数最少的
                if tnum == 0:
                    return step + 1
                # 只添加没有遍历过的节点
                if not visited[tnum]:
                    q.append((tnum, step + 1))#（16，1） （7，1 ，（0，1#可能的情况-4  -9  -16
                    visited[tnum] = True
                i += 1
                tnum = num - i ** 2 #16-4 16-9  16-16