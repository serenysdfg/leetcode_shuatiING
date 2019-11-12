#23min
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # copy
        # 就是先统计words中字符串最小字母出现频次，然后将它排序得到w数组。这样我们在统计queries中字符串最小字母出现频次i的时候，这样我们就可以通过upper_bound计算出在w中比i大的第一个位置。
        # w = sorted([i.count(min(i)) for i in words])
        # return [len(w) - bisect.bisect_right(w, i.count(min(i))) for i in queries]#返回bisect_right将会插入的位置
        # copy2
        q = [i.count(min(i)) for i in queries]
        w = [i.count(min(i)) for i in words]
        res = []

        for i in range(len(queries)):
            k = 0
            for j in range(len(words)):
                if q[i] < w[j]:
                    k += 1
            res.append(k)
        return res

#         # 3<4   2<3或者4（2个）#超时
#         def f(word):
#             a=sorted(word)
#             count=1
#             i=0
#             if len(word)==1:return 1 #忽略了
#             while i<len(a)-1:
#                 if a[i]==a[i+1] :
#                     count+=1
#                     i+=1
#             return count
#         b=[]
#         answer=[]
#         for i in words:
#             b.append(f(i))
#         b.sort()

#         for q in queries :
#             for i in range(len(b)):
#                 if b[i]>f(q):
#                     answer.append(len(b[i:]))
#                     break

#         return answer