class Solution:
    def myAtoi(self, str: str) -> int:


#         #很多小bug，30min 需要考虑比较多的边界条件&特殊情况
#         a=''
#         p=-1
#         for i in range(len(str)):
#             if str[i]!=" ":
#                 p=i
#                 break   #str.strip()
#         if p==-1:  #全都是空，没有赋值
#             return 0

#         if str[p]=='+' or str[p]=='-': #positive = True #正负标志
#             a+=str[p]
#             p+=1
#         elif ord(str[p])<48 or ord(str[p])>57:
#             return 0
#         for i in range(p,len(str)):
#             if ord(str[i])>=48 and ord(str[i])<=57: #char >='0' and char <='9':
#                 a+=str[i]
#                 print(a)
#             else:#返回 
#                 break
#         if a=='+' or a=='-':
#             return 0
#         if int(a)>pow(2,31)-1 :
#             return pow(2,31)-1
#         elif int(a)<-pow(2,31):
#             return -pow(2,31)
#         else:
#             return int(a)
'''需要考虑比较多的边界条件&特殊情况

首先输入可能会有空格，所以先去掉空格
去掉空格后要考虑空字符串情况
字符串首位可能会有正负号，要考虑
开始转换成数字，题目说只要遇到非数字就可以break了
结果太大或者太小超过int限制就要返回特定数字 2147483647 或者 -2147483648
根据之前的正负号结果返回对应数值'''


class Solution:
    def myAtoi(self, str: str) -> int:

        str = str.strip()
        strNum = 0
        if len(str) == 0:  # 空字符
            return strNum

        positive = True  # 正负标志
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                positive = False
            str = str[1:]

        for char in str:
            if char >= '0' and char <= '9':
                strNum = strNum * 10 + ord(char) - ord('0')  # 直接赋值
            if char < '0' or char > '9':
                break

        if strNum > 2147483647:
            if positive == False:
                return -2147483648
            else:
                return 2147483647
        if not positive:
            strNum = 0 - strNum
        return strNum