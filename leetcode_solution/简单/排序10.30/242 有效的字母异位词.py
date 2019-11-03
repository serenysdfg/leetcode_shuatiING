给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #me
        if len(s)!=len(t):return False
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        return s==t
    #一行
        return collections.Counter(s) == collections.Counter(t) #1
        return sorted(s) == sorted(t)#2
    #3字数统计
        if len(s) != len(t):
            return False
        
        charCnt = [0] * 26
        
        for i in range(len(s)):
            charCnt[ord(s[i]) - 97] += 1
            charCnt[ord(t[i]) - 97] -= 1 
        
        for cnt in charCnt:
            if cnt != 0:
                return False
        return True
  #4
        for i in range(ord('a'), ord('z')+1):
            if s.count(chr(i)) != t.count(chr(i)): #s.count('a') ,ord('a')
                return False
        return True
