''''''
'''如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。

例如，321 是一个步进数，而 421 不是。

给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。

示例：

输入：low = 0, high = 21
输出：[0,1,2,3,4,5,6,7,8,9,10,12,21] 

'''
class Solution:
    def countSteppingNumbers(self, l: int, r: int) -> List[int]:
        res = []

        def bfs(s):
            q = [s]
            while len(q):
                pre = q.pop(0)
                if pre <= r and pre >= l:
                    res.append(pre)
                if pre == 0 or pre > r:
                    return

                lt = pre % 10
                s1, s2 = pre * 10 + lt - 1, pre * 10 + lt + 1
                if lt == 0:
                    q.append(s2)
                elif lt == 9:
                    q.append(s1)
                else:
                    q.append(s1)
                    q.append(s2)

        for i in range(10):
            bfs(i)
        return sorted(res)
