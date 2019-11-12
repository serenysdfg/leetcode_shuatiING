class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        #copy双指针
        n = len(s)
        start, end = 0, n - 1

        while start < end:
        	s[end], s[start]  = s[start],s[end]#互换
        	start += 1
        	end -= 1
