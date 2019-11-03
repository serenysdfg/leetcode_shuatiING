#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (63.21%)
# Total Accepted:    9.2K
# Total Submissions: 14.5K
# Testcase Example:  '"A"'
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 
# 例如，
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: "A"
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: "AB"
# 输出: 28
# 
# 
# 示例 3:
# 
# 输入: "ZY"
# 输出: 701
# 
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
# 
#
# AB -- A=1 B=2AB=A*26+B=28
#  ZY -Z=26Y=25 ZY=Z*26+Y=701
#  ABA -- A=1 B=2 A=1 AAB=A*26*26+B*26+A=729
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 初始化映射关系
        char_dict=dict()
        for i in range(26):
            char_dict[chr(i+ord('A'))]=i+1
            #遍历列名
        num,base=0,1
        for i in range(len(s)):
            char_idx=len(s)-i-1
            char=s[char_idx]
            num+=char_dict[char]*base
            base=base*26
        return num
        

