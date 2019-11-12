class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # copy1
        mapx = {}
        for i in strs:
            x = ''.join(sorted(list(i)))  # 转换相同的
            if x in mapx:
                mapx[x].append(i)
            else:
                mapx[x] = [i]
        return mapx.values()

# #不太好用counter也可以，不继续做

