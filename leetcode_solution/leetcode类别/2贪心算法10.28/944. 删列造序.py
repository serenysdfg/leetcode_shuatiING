class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        #copy
        return sum(list(a) != sorted(a) for a in zip(*A)) #获取序列 zip(*A) ，不是升序就是1