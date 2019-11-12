class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace(",", " ").replace(";", " ").replace(".",
                                                                                                              " ").replace(
            "'", " ")  # 叹号问号，逗号句号，分号引号
        a = paragraph.split(' ')  # 要去掉逗号
        words = [i.lower() for i in a]
        dict = {}
        for i in words:
            dict[i] = dict.get(i, 0) + 1
        # 去掉banned
        dict[''] = 0  # 意外
        for i in banned:
            dict[i] = 0
        # 字典中找到排序
        maxnum = sorted(dict.values())[-1]  # 字典排序,最大的
        return [i for i in dict if dict[i] == maxnum][0]

    # copy非禁用词就是1
# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):
#         """
#         :type paragraph: str
#         :type banned: List[str]
#         :rtype: str
#         """
#         para=paragraph.lower()
#         para+=' '
#         res=''
#         words=[]
#         #提取字符
#         for i in para:
#             if i.isalpha():
#                 res+=i
#             else:
#                 if len(res)!=0:
#                     words.append(res)
#                     res=''
#         dic={}
#         flag=''#当前非禁用词
#         times=0#非禁用词出现的次数
#         for word in words:
#             if word not in dic:
#                 dic[word]=1
#             else:
#                 dic[word]+=1
#         for i,j in dic.items(): #获取最大的，并记录，更改
#             if i not in banned:
#                 if j>times:
#                     times=j
#                     flag=i
#         return flag