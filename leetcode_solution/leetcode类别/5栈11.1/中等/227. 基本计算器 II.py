'''实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。'''
class Solution:
    def calculate(self, s: str) -> int:
        #copy1
        # https://mp.weixin.qq.com/s/rVLUDzoEwb796eGVRdYSgA
        # 具体计算过程为: 从前往后遍历, 当遇到整数或者 +/ -时, 将其存储到一个栈中, 当遇到 *或者 /时, 取出栈顶, 将指针向前移动一位, 将结果加到栈顶, 继续往前遍历.（乘除先计算，加减的放后面

        #copy2
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = 0
                while i < len(s) and s[i].isdigit():#连续数字，可能二位或者三位
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                stack.append(tmp)
                # 如果栈中有乘除，先算出来
                while len(stack) > 1 and stack[-2] in {"*", "/"}:
                    stack.pop()
                    opt = stack.pop()
                    if opt == "*":
                        stack.append(stack.pop() * tmp)
                    else:
                        stack.append(stack.pop() // tmp)
            elif s[i] in { "*", "/", "+", "-"}:
                stack.append(s[i])
                i += 1
            else: #空格
                 i += 1
        res = 0
        sign = 1
        for t in stack:
            if t == "+":
                sign = 1
            elif t == "-":
                sign = -1
            else:
                res += sign * t
        return res