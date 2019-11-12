给定一个只包括
'('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合



class Solution:
    def isValid(self, s: str) -> bool:
        # copy
        stack = list()
        match = {'{': '}', '[': ']', '(': ')'}  # 建立字典,pop出的和下一个非左边不对应
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if match[top] != i:
                    return False

        return len(stack) == 0
        # 失败
#         stack[]
#         for  i in range(len(s)):
#             if s[i]=="(" or s[i]=="{" o s[i]=="[":
#                 stack.append(s[i])
#             elif s[i]==")":
#                 if stack.pop()!="("
#                  or s[i]=="}" o s[i]=="]":
