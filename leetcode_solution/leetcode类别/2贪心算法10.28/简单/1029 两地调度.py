class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: abs(x[0]-x[1]), reverse=True)    #绝对值相减排序，只要获取总和，无所谓顺序
        n = len(costs)//2  
        i, j = 0, 0
        res = 0
        for cost in costs: #先选取绝对差值大的小数
            if cost[0]<cost[1] and i<n : #前面的小，人数没够
                res += cost[0]
                i += 1
            elif j<n: #人数够了，或者后面的小
                res += cost[1]
                j += 1
            else: #后面的满了，虽然前面大也要前面的
                res += cost[0]
        return res
        #失败
#         sum=0
#         a=0
#         b=0
#         for i in range(len(costs)):
#             if costs[i][0]<=costs[i][1] and a<len(costs)/2 and b<len(costs)/2:
#                 sum+=costs[i][0]
#                 a+=1
#                 continue #不执行这一轮

#             elif costs[i][0]>costs[i][1] and a<len(costs)/2 and b<len(costs)/2:
#                 sum+=costs[i][1]
#                 b+=1
#                 continue
#             if a==len(costs)/2:
#                 sum+=costs[i][1]
#             elif b==len(costs)/2:
#                 sum+=costs[i][0]
#         return sum
                
                