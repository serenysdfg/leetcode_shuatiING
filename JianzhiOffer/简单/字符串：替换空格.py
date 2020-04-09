#简单
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s=s.split(' ')
        return '%20'.join(s)
#copy
class Solution:
    '''将字符串中的空格替换成%20'''
    # str为源字符串
    def replaceSpace(self, str):
        return str.replace(' ', '%20')