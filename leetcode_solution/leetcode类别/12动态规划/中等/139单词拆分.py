#未仔细看
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # lose:字典在中一次次递归 递归lose，也不是重复有的多次
        # def rep(s,wordDict):
        #     for sw in wordDict:
        #         if sw in s:
        #             s=s.replace(sw,'')
        #         else:
        #             return s
        #     return s

        # while s!='':
        #     s1=s
        #     s=rep(s1,wordDict)
        #     if s1==s:
        #             return False
        #     else:
        #         s1=rep(s,wordDict)
        #     if not s:return False

        # return True
        # 超时https://blog.csdn.net/qq_17550379/article/details/82933187
        return self._wordBreak(s, set(wordDict), 0)

    def _wordBreak(self, s, words, start):
        if start == len(s):
            return True

        for i in range(start + 1, len(s) + 1):
            sub = s[start:i]
            if sub in words and self._wordBreak(s, words, i):
                return True

        return False

#         #copy1
#         ok = [True]
#         for i in range(1, len(s)+1):
#             ok += [any(ok[j] and s[j:i] in wordDict for j in range(i))]
#         return ok[-1]

# #copy2
#         ok = [True]
#         for i in range(1, len(s)+1):
#             ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
#         return ok[-1]