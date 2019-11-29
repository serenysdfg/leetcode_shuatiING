class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''后续再看和思考
        二维表格dp的大小为（len(s)+1）*(len(p)+1)，dp[i][j]表示，若s的子串[0,i）和p的子串[0，j）匹配，dp[i][j]=True ，若不匹配dp[i][j]=False。最后返回的就是右下角位置的数字。
      当 p 为空串时，只有目标串 s 的空串才能与 p 匹配；
      当 s 为空串时，只有 p 为 空串 或者 为 x*y* 的形式才能与 s 匹配。
https://blog.csdn.net/weixin_39781462/article/details/82999610
  '''
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]  # 初始化二维表dp
        print(dp)
        dp[0][0] = True  # s 和 p 都为空时
        #  若 s 为空时
        for j in range(1, len(p) + 1):
            # dp[0][j]= (p[j-1]=="*")and(j>=2)and(dp[0][j-2])            #  等同于下列语句
            if p[j - 1] == '*':
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]
        print(dp)

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #  j-1才为正常字符串中的索引
                #  p当前位置为"*"时，(代表空串--dp[i][j-2]、一个或者多个前一个字符--( dp[i-1][j] and (p[j-2]==s[i-1] or p[j-2]=='.'))
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (
                                dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))  # dp[i][j-1] or
                #  p当前位置为"."时或者与s相同时，传递dp[i-1][j-1]的真值
                else:
                    dp[i][j] = (p[j - 1] == '.' or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]

        return dp[len(s)][len(p)]

        # copy1递归
        # if p == "":# 判断匹配规则是否为空  递归
        #     return s == ""
        # if len(p) > 1 and p[1] == "*":
        #     return self.isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        # else:
        #     return s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])

        # if p == "":
        #     return s == ""  # p为空的时候，判断s是否为空，则知道返回True 或 False
        # if len(p) == 1: #特殊
        #     return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        # if p[1] != "*":#不为*则必须有字符
        #     if s == "":
        #         return False
        #     return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])#下一个# 递归
        #     #2
        # while s and (s[0] == p[0] or p[0] == '.'): #到了while循环，说明p[1]为*  递归调用匹配s和p[2:](*号之后的匹配规则)
        #     if self.isMatch(s, p[2:]):# 把a*相关的都弄完了，匹配p[2:]和s中a*之后的元素
        #         return True    
        #     s = s[1:]# 当匹配字符串和匹配规则*都能匹配的时候，去掉第一个字符成为新的匹配字符串，循环     
        # return self.isMatch(s, p[2:])
        # copy2动态


