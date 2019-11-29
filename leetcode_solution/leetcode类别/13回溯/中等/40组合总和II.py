class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(remain, combo, index):
            if remain == 0 and combo not in res:#不重复
                res.append(combo)#找到
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:#找不到不要
                    break          
                dfs(remain - candidates[i], combo + [candidates[i]], i+1)#i+1 #不重复

        candidates.sort()
        res = []
        dfs(target, [], 0) 
        return res