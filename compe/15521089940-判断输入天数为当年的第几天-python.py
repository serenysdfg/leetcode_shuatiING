'''>初级赛题：判断输入天数为当年的第几天

·题目介绍

输入一个日期，格式为xxxx-xx-xx，判断这一天为当年的第几天？

·示例

输入：2019-1-2

输出：2'''
class Solution:
    def calday(date):
        da=date.split('-')
        year,month,day=da[0],da[1],da[2]
        days_shuzu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        calday = sum(days_shuzu[:month - 1]) + day
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month>3:
            calday +=1
        return calday
#example
# Solution.calday("2020-12-31")  #366
# Solution.calday("2019-12-31") #365
