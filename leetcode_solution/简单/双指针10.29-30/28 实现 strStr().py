class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":return 0
        if (needle in haystack):
            return haystack.find(needle  )
        else:
            return -1