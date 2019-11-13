class Solution:
    def calculate(self, s: str) -> int:        #copy1
        '''解题思路

经典问题，首先采用递归的方式求解。这里使用了trick，使用1表示加法，使用-1表示减法，使用l表示左值，使用r表示右值。

当遍历到的字符是'('的时候我们需要递归下去，同时计算左值l += op * dfs()。
当遍历到的字符是')'的时候，返回结果l + op * r。
当匹配到+-的时候需要调整操作符op，同时需要更新此时的左值l += op * r。
当匹配到空格的时候跳过。
当匹配到数字的时候，更新右值r = r * 10 + int(s[u])，其中u表示当前的位置。
当所有元素都遍历完后，返回l + op * r。
————————————————
原文链接：https://blog.csdn.net/qq_17550379/article/details/102844303'''
        u, s_len = 0, len(s)
        def dfs():
            nonlocal u
            l, r, op = 0, 0, 1
            while u < s_len:
                if s[u] == ' ':
                    u += 1
                    continue
                elif s[u] in '+-':
                    l += op * r
                    r, op = 0, 1 if s[u] == '+' else -1
                    u += 1
                elif s[u] == '(':
                    u += 1
                    l += op * dfs()
                elif s[u] == ')':
                    u += 1
                    return l + op * r
                else:
                    r = r * 10 + int(s[u])
                    u += 1
            return l + op * r
        return dfs()

                #copy2
        '''
        当前字符为 (/ +/ -, 那么直接 push进去
当前字符为 ), 将前面的元素依次 pop出来, 直到遇到 (为止, 计算中间表达式的结果(递归),将值 push进去

'''
    #     res=stack.pop() if stack else 0
    #     while stack and stack[-1]!=')':
    #         sign=stack.pop()
    #         if sign=='+':
    #             res+=stack.pop()
    #         else:
    #             res-=stack.pop()
    #     return res
    # def calculate(self, s: str) -> int:
    #     #copy
    #     stack=[]
    #     n,ope=0,0
    #     for i in range(len(s)-1,-1,-1):#遇到左括号开始计算，所以先从后往前
    #         ch=s[i]
    #         if ch.isdigit():
    #             #反转
    #             ope=(10**n*int(ch))+ope
    #             n+=1
    #         elif ch!=" ":
    #             if n:
    #                 #在ope保存stack
    #                 stack.append(ope)
    #                 n,ope=0,0
    #             if ch=='(':
    #                 res=self.evaluate_expr(stack) #遇到左括号，计算栈里面的值
    #                 stack.pop()
    #                 stack.append(res)
    #             else:
    #                 stack.append(ch)
    #     if n:
    #         stack.append(ope)
    #     return self.evaluate_expr(stack)
'''copy3
同样也可以使用递归解决，递归我们也使用了trick，只使用一个栈就解决了。算法思路和上面的方法类似，只是当访问的元素是'('的时候，
将l和op添加到栈中，同时更新op=1、l=0。当访问的元素是')'的时候，将栈中的l和op弹出，并且更新l'''
class Solution:
    def calculate(self, s):
        st, op, r, l = [], 1, 0, 0
        for c in s:
            if c.isdigit():
                r = r * 10 + int(c)
            elif c in "+-":
                l += op * r
                r, op = 0, 1 if c == '+' else -1
            elif c == "(":
                st.append(l)
                st.append(op)
                op, l = 1, 0
            elif c == ")":
                l += op * r
                r = 0
                l = st.pop() * l + st.pop()
        return l + op * r
