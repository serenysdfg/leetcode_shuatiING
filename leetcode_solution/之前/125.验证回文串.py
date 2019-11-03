#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (38.75%)
# Total Accepted:    30K
# Total Submissions: 77.3K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        if(len(s)==0):
            return True
        l=0
        r=len(s)-1
        while(l<r):
            if(not  s[l].isdigit and  not s[l].islower()):
                l+=1
                continue
            if (not  s[r].isdigit and  not s[r].is()):
                r-=1
                continue
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        

