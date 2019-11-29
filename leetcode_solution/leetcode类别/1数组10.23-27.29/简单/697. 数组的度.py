class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # copy
        left, right, count = {}, {}, {}  # 左右代表，一个数字第一次出现和最后一次出现 count字典计数
        for i, v in enumerate(nums):
            if v not in left.keys():
                left[v] = i
            right[v] = i
            count[v] = count.get(v, 0) + 1

        degree = max(count.values())  # 求元素最大出现次数
        ret = len(nums)
        for k, v in count.items():
            if v == degree:
                ret = min(ret, right[k] - left[k] + 1)
        return ret

        # d={}
        # for s in nums:
        #     d[s]=d.get(s,0)+1
        # m=0
        # for key,value in d.items():
        #     if value>m:
        #         m=value
        #         mkey=key
