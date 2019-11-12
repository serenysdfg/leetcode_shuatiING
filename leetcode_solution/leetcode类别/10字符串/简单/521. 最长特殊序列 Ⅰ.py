class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        #相同肯定有子串
#         如果两个字符串A和B，如果A比B的长度大，那么A肯定不能由B删除某些字符得到啊，那么A的长度肯定就是这个最大长度了。

# 其次，如果A和B等长的话，看他们是不是相等的，如果相等的那么一个字符串肯定能由另外一个字符串不用删除都等得到啊。

# 最后如果A和B等长并且他们还不相等，那么其中字符串A肯定就不能由字符串B删除字符之后得到，因为人家本来长度都相等了，你再删除肯定短了嘛，不可能再相等了。

        if a == b:
            return -1
        else:
            if len(a)>len(b):
                return len(a)
            else:
                return len(b)