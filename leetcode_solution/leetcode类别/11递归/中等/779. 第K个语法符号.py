class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        '''我们没有必要求出来整个字符串是什么样子，比如我们求第11行的1000个数字是0还是1，那么第11行的第1000个数字 a 是根据哪儿来的呢，是依照第10行的第500个数字 b 而来，如果 b 为 0 ，那么 a 为 1，否则 a 为 0； b 又是依照 9行250个数字 c 来，数字才依照 8 行 125数字 d 来， d 依照 7 行 63 e 来（125,126都是根据e，但不同的是 e 比方说为0 ， 那么 125 126分别为 0 1）……按此规律下去。

当 k 为偶数时，它的值 = n-1行的 k/2  == 0 ？ 1 ：0 

当 k 为奇数时，它的值 = n-1行的 (k+1)/2 == 0 ?  0 : 1 
'''

        # if 1==N:
        #     return 0
        # tmp=2**(N-1)
        # flag=0
        # while N>1:
        #     tmp>>=1
        #     if K>tmp:
        #         flag=1-flag
        #         K-=tmp
        #     N-=1
        # if flag:
        #     return 1

#规律，和N无关
        def getN(K):
            if K == 0:
                return 0
            elif K == 1:
                return 1
            else:
                if getN(int(K/2)) == 0: #递归
                    if K % 2 == 0:
                        return 0
                    else:
                        return 1
                else:
                    if K % 2 == 0:
                        return 1
                    else:
                        return 0
        return getN(K-1)


