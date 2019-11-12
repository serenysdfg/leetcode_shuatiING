# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         #set去重。，正则不行
#         a=[]
#         for e in emails:
#             i=0
#             # q=0
#             p=None #失误，p不一定存在，后面p
#             for i in range(len(e)):
#                 if e[i]=='@':
#                     q=i
#                     break #不去计数
#                 i+=1
#             for i in range(q):
#                 if e[i]=='+': #未考虑，有多个+
#                     p=i
#                     break

#             #计算+前面去掉.
#             if not p:
#                 p=q
#             m=e[:p]
#             m=m.replace('.','')
#             a.append( m+e[q:])
#         return len(set(a))
# copy
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        em = []
        for i in range(len(emails)):
            flag = True
            s = ""
            for j in range(len(emails[i])):
                if emails[i][j] == '.' and flag:
                    continue
                elif emails[i][j] == "@":
                    flag = False
                    s = s + emails[i][j]
                else:
                    s = s + emails[i][j]
            em.append(s)

        list = []
        for i in range(len(em)):
            s = ""
            flag = True
            for j in range(len(em[i])):
                if em[i][j] == '+':
                    flag = False
                    continue
                elif em[i][j] == "@":
                    flag = True
                if flag:
                    s = s + em[i][j]

            if s not in list:
                list.append(s)

        return len(list)