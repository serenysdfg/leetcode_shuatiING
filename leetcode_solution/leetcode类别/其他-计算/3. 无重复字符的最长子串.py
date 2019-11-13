# 定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

#不懂
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # copy粗一看是dp，细一看是greedy贪心，没看懂
        # 我们先从第一个字符开始，只要碰到已经出现过的字符我们就必须从之前出现该字符的index开始重新往后看。
        # 只要目前的这个字符在该hashmap中的值大于等于了这一轮字符串的首字符，就说明它已经出现过了，我们就将首字符的index加1，即从后一位又重新开始读，然后比较目前的子串长度与之前的最大长度，取大者。
        '''
l(字母L) 代表目前最大子串的长度
start 是这一轮未重复子串首字母的index
maps 放置每一个字符的index，如果maps.get(s[i], -1)大于等于start的话，就说明字符重复了，
此时就要重置 l(字母L) 和start的值了，
    '''
        l, start, n = 0, 0, len(s)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(s[i], -1) + 1)
            l = max(l, i - start + 1)
            maps[s[i]] = i
        return l

#         start = maxLength = 0
#         usedChar = {}
#         for index, char in enumerate(s):
#             if char in usedChar and start <= usedChar[char]:
#                 start = usedChar[char] + 1
#             else:
#                 maxLength = max(maxLength, index - start + 1)
#             usedChar[char] = index
#         return maxLength