class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 字典,一个加一个减

        map1 = {}
        for i in magazine:
            map1[i] = map1.get(i, 0) + 1  # map1[i]+=1
        for i in ransomNote:
            if i not in map1 or map1[i] == 0:
                return False
            else:
                map1[i] -= 1
        return True

