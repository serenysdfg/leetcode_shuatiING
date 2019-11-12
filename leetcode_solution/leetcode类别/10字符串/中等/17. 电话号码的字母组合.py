class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # copy2
        if not digits:
            return []

        l_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        chars = [l_map.get(d) for d in digits]
        return [''.join(x) for x in itertools.product(*chars)]
        # copy
#      s用来记录结果，每次从digits里面去一个，然后寻找其可能的char，加到s中，digits长度减小
# digits长度为0时候，把它加入结果
#     if digits == '':
#         return []
#     self.res = []
#     self.singleResult('', digits)
#     return self.res

# def singleResult(self, s, digits):#回溯法
#     if len(digits) == 0:
#         print(s)
#         self.res.append(s)
#     else:
#         mapx = {'2':['a','b','c'],
#             '3':['d','e','f'],
#             '4':['g','h','i'],
#             '5':['j','k','l'],
#             '6':['m','n','o'],
#             '7':['p','q','r','s'],
#             '8':['t','u','v'],
#             '9':['w','x','y','z']}
#         cur_digit = digits[0] #第一个数字
#         for c in mapx[cur_digit]:#第一个数字对应的每一个字母a或者b或者c
#             self.singleResult(s+c, digits[1:])#每个数字中选一个 字母

# #me 22题意不清，失败
# d1={
#     '2':['a','b','c'],
#     '3':['d','e','f'],
#     '4':['g','h','i'],
#     '5':['j','k','l'],
#     '6':['m','n','o'],
#     '7':['p','q','r','s'],
#     '8':['t','u','v'],
#     '9':['w','x','y','z']
# }
# a=[]
# if len(digits)==1:return d1[digits[0]]
# # d1[digits[0]][0]+d1[digits[1]][0]+d1[digits[2]][0] #两个参数
# for i in [0,1,2]:
#     ss=''
#     for j in range(len(digits)):
#         ss+=d1[digits[j]][i]#

        result = list()
        if not digits:
            return result

        l_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        chars = [l_map.get(d) for d in digits]
        tmp = [[]]
        for pool in chars:
            tmp = [x + [y] for x in tmp for y in pool]

        for prod in tmp:
            result.append(''.join(prod))

        return result
