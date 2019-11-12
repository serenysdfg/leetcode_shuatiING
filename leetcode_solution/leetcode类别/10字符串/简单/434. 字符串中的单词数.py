class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split(" ")
        return len(s) - s.count("")#去掉空格