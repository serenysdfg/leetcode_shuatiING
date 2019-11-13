'''解题思路
以示例 1为例, 表达式为 2-1-1, 分析一下: 从前往后遍历:

第一个字符为 2, 不为符号, 继续往前

第二个字符为 -, 为符号, 那么需要计算前后表达式的值( 2和 1-1, 递归调用)

首先, 计算表达式 2的值, 直接返回 2

接着, 1-1表达式的值: 同理, 也需要计算前后表达式的值: 返回 0

针对返回的两个列表: [2]和 [0], 直接相减就继续往前遍历了

第三个字符为 1, 也不为符号, 继续向前

第四个字符为 -, 为符号, 同样需要计算前后表达式的值( 2-1和 1, 也递归调用)

首先, 计算表达式 2-1的值, 返回 1

接着, 表达式 1, 直接返回 1

针对返回的两个列表: [1]和 [1], 得到结果为 0

这是个比较简单的例子, 再看看示例 2: 2*3-4*5, 看看遇到第一个符号 *时, 我们需要计算表达式 2和 3-4*5的值, 我们可以看到第二个表达式也有多种可能的结果, 因此需要调用递归解决, 返回的是一个 list.

另外, 我们发现当表达式相同的时候, 其实可以直接返回已经计算过的结果, 避免重复计算, 因此, 可以使用一个 dict将计算过的表达式存起来, 之后如果需要取的时候直接返回即可.
'''

class Solution:
    def __init__(self):
        self.exp_dict={}
    def diffWaysToCompute(self, input: str) -> List[int]:
        #copy11.13

        if input in self.exp_dict:
            return self.exp_dict[input]
        res_list=[]
        for i in range(len(input)):
            if input[i] in ['+','-','*']: #第二个字符为 -, 为符号, 那么需要计算前后表达式的值( 2和 1-1, 递归调用
                l_input=input[:i]
                r_input=input[i+1:]
                l_list=self.diffWaysToCompute(l_input)
                r_list=self.diffWaysToCompute(r_input)
                for  l_res in l_list: #计算
                    for r_res in r_list:
                        res=0
                        if input[i]=='+':
                            res=l_res+r_res
                        elif input[i]=='-':
                            res=l_res-r_res
                        elif input[i]=='*':
                            res=l_res*r_res
                        res_list.append(res)
        if len(res_list)==0:
            res_list.append(int(input))
        self.exp_dict[input]=res_list
        return res_list