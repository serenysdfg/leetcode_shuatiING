'''>中级赛题："水仙花数"判断
·题目介绍
输入一个三位数判断是否为"水仙花数"，水仙花数指该三位数每个位上的数字立方和等于它本身，即A³+B³+C³=ABC
·示例
输入：153
输出：Ture'''

class Solution:
    def shuixianhua(num):
        sum,n=0,num
        while n!=0:
            sum += pow(n % 10, 3)
            n=n//10
        if sum==num:return True
        else:return  False
# Solution.shuixianhua(153) :True
# Solution.shuixianhua(156) :False