class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # copy如果左括号已经用完了，则不能再加左括号了。
        # 如果已经出现的右括号和左括号一样多，则不能再加右括号了。因为那样的话新加入的右括号一定无法匹配。
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res

    def singleStr(self, s, left, right, n):
        if left == n and right == n:  # 一种结果
            self.res.append(s)
        if left < n:
            self.singleStr(s + '(', left + 1, right, n)  # 递归后面情况
        if right < left:
            self.singleStr(s + ')', left, right + 1, n)  # 也递归
        # copy2
        ans = []

        def dp(s, l, r):
            if len(s) == n * 2:  # 结束
                ans.append(s)
                return
            else:
                if l < n:
                    dp(s + "(", l + 1, r)
                if r < l:
                    dp(s + ")", l, r + 1)

        dp("", 0, 0)
        return ans

