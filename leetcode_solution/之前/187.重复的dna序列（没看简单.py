#
# @lc app=leetcode.cn id=187 lang=python
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (41.54%)
# Total Accepted:    2K
# Total Submissions: 4.9K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。
# 
# 示例:
# 
# 输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# 输出: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
#
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret_list = []
        char_size = 10
        for i in range(len(s) - char_size):
            cur_str = s[i: i + char_size]
            if cur_str not in ret_list and cur_str in s[i+1:]:
                ret_list.append(cur_str)
        return ret_list
        

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret_list = []
        char_size = 10
        for i in range(len(s) - char_size):
            cur_str = s[i: i + char_size]
            if cur_str not in ret_list and cur_str in s[i+1:]:
                ret_list.append(cur_str)
        return ret_list


#     def findRepeatedDnaSequencesBit(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         if len(s) <= 10:
#             return []
#         mask = 0x7ffffff
#         cur = 0
#         str_dict = dict()
#         ret_list = list()
#         for i in range(9):
#             cur = (cur << 3) | (ord(s[i]) & 7)
#         for i in range(9, len(s)):
#             cur = ((cur & mask) << 3) |  (ord(s[i]) & 7)
#             if cur in str_dict:
#                 cnt = str_dict[cur]
#                 if cnt == 1:
#                     ret_list.append(s[i-9:i+1])
#                 str_dict[cur] += 1
#             else:
#                 str_dict[cur] = 1
#         return ret_list
# sl = Solution()
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# print(sl.findRepeatedDnaSequences(s))
# print(sl.findRepeatedDnaSequencesBit(s))
# s = "AAAAAAAAAAAA"
# print(sl.findRepeatedDnaSequences(s))
# print(sl.findRepeatedDnaSequencesBit(s))
# ['AAAAACCCCC', 'CCCCCAAAAA']
# ['AAAAACCCCC', 'CCCCCAAAAA']
# ['AAAAAAAAAA']
# ['AAAAAAAAAA']