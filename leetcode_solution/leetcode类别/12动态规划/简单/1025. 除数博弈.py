import math


class Solution:
    def divisorGame(self, N: int) -> bool:
        # copy有规律一个个增长
        # 1归纳法
        # return N % 2 == 0
        # 2dp如果i的约数里面有存在为False的（即输掉的情况），则当前i应为True；如果没有，则为False。尽力让对方输掉
        target = [0 for i in range(N + 1)]  # 0是输
        target[1] = 0  # 若爱丽丝抽到1，则爱丽丝输
        if N <= 1:
            return False
        else:

            target[2] = 1  # 若爱丽丝抽到2，则爱丽丝赢
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
                    if i % j == 0 and target[i - j] == 0:  # 让对方输
                        target[i] = 1
                        break
            return target[N] == 1
