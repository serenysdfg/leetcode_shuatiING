class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #
        def dfs(remain, combo, index):
            if remain == 0:
                res.append(combo)#找到
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:#找不到不要
                    break          
                dfs(remain - candidates[i], combo + [candidates[i]], i)#i还可以继续从本位置开始
        # candidates = list(set(candidates))#不重复
        candidates.sort()
        res = []
        dfs(target, [], 0) #重要，，剩余，列表[],index从第几个
        return res