'''给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

'''
class Solution:
    def numTrees(self, n: int) -> int:
        # 不用构造？？
        # dp动态规划
        '''
        动态规划
        假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数即有: G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
        当i为根节点时，其左子树(个数为i - 1)节点个数为[1, 2, 3, ..., i - 1]，右子树(n - i个)节点个数为[i + 1, i + 2, ... n]，
         右子树节点为n - i，即f(i) = G(i - 1) * G(n - i),
        上面两式可得: G(n) = G(0) * G(n - 1) + G(1) * (n - 2) + ... + G(n - 1) * G(0)

'''
        mem = [0] * (n + 1)
        mem[0], mem[1] = 1, 1

        for i in range(2, n + 1):
            mem[i] += mem[j - 1] * mem[i - j]
        # 状态转移公式：dp(n) = dp(0)*dp(n-1)+dp(1)*dp(n-2)+...+dp(n-1)*dp(0)
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                mem[i] += mem[j - 1] * mem[i - j]  # j-1从0到n-1

        return mem[-1]