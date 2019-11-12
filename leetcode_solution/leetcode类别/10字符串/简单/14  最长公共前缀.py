class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #copy
        # if not strs:
        #     return ''
        # for i, word in enumerate(zip(*strs)):
        #     if len(set(word)) > 1:
        #         return strs[0][:i]#返回前缀
        # else:#全都《1
        #     return min(strs)
        #copy2一个个循环长度-1
        if strs:
            strs.sort(key=len)
            a = strs[0]
            len1 = len(a)
            for i in strs:
                if a[:len1] == i[:len1]:
                    continue
                else:
                    while True:
                        len1 -= 1
                        if a[:len1] in i[:len1] :
                            break
                        if len1 ==0:
                            return ""
            return a[:len1]
        else:
            return ""