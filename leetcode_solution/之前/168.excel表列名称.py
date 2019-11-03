#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (29.92%)
# Total Accepted:    5.2K
# Total Submissions: 17.4K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#
# 解题思路

# 查阅示例, 可以看出 1-26直接对应 A-Z,那么接下来呢? 找规律:
# 这样就找到规律了, 如果当前数值大于 26那么就迭代, 使用其与 26的商和余数继续拼接. 这里需要注意一个地方: 当整数是 26的倍数的时候, 不应该使用商进行迭代, 而应该是商减去 1, 然后余数直接设置为 26即可.
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mark=[chr(i+ord('A')) for i in range(26)]
        if n>0 and n<=len(mark):
            return mark[n-1]
        left=int(n/26)
        right=n%26
        if right==0:
            left-=1
            right=26
        return convertToTitle(left)+convertToTitle(right)
        

