给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
'''
方法1: 排序法

变位词的意思是: 重新组织字符串 s的字母顺序为 t. 因此, 如果 t是 s的一个变位词的话, 对字符串排序之后得到的结果字符串应该是完全相同的. 此外, 如果 t和 s的字符串长度不一样的话, 就可以直接返回 false了.

复杂度方面: 时间复杂度为: O(nlogn), 其中 n为 s的长度, 排序的时间复杂度为 O(nlogn)而比较字符串的时间复杂度为 O(n), 因此总时间复杂度为 O(n). 空间复杂度为 O(1), 主要根据排序中占用的时间复杂度来确定.

方法2: 计数数组法

其实还有一个最简单的方法: 使用一个字典来存储两个字符串中出现的字符以及对应的次数. 但是前面提到只包含小写字母, 直接使用一个数组来存储对应的计数即可. 第一次遍历时, 对于 s中的字符, 直接将对应的元素 +1, 对于 t中的字符, 将对应的元素 -1. 最后遍历一遍 counter, 看是不是所有元素都为 0即可.

还有一种小优化, 在第一次遍历的时候只更新 s的元素, 而在第二次遍历更新的时候, 只需要判断一下是否有小于 0的元素即可. 由于前面判断了字符串的长度, 因此如果有不相同字符的话, 必定会出现至少一个负值. 如果正常到了最后, 直接返回 true.

时间复杂度: O(n), 空间复杂度为 O(1).'''

#字符串
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        for i in s:
            maps[i] = maps.get(i, 0) + 1
        for i in t:
            maps[i] = maps.get(i, 0) - 1
        for cnt in maps:
            if maps[cnt] != 0:
                return False
            # if maps[i]<0: #还有a多的情况

        return True
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
#####2

