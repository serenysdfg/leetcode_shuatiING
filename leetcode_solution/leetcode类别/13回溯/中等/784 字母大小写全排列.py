class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        #copy回溯
    res = []
    self.dfs("", S, res, 0)
    return res

def dfs(self, pre, S, res, index):
    """
    :type pre: str
    :type S: str
    :type res: List[str]
    :type index: int
    :rtype: None
    """
    if index == len(S):
        res.append(pre)
    else:
        ch = S[index]
        if str.isdigit(ch):
            self.dfs(pre + ch, S, res, index + 1)
        else:
            ch = str.lower(ch)
            self.dfs(pre + ch, S, res, index + 1)

            ch = str.upper(ch)
            self.dfs(pre + ch, S, res, index + 1)



        #copy
        # list1 = [S]

        # for i in range(len(S)):
        #     list2 = []
        #     for s in list1:
        #         if  s[i].isdigit():
        #             list2.append(s)#数字直接加
        #         else:
        #             list2.append(s[0:i]+s[i].upper()+s[i+1:])#遍历到字母改为大写
        #             list2.append(s[0:i]+s[i].lower()+s[i+1:])#遍历到字母改为小写
        #     list1 = list2
        # return list1
