class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # me1
        # d={}
        # a,b=0,0
        # for i in range(len(secret)):
        #     d[i]=secret[i]
        # li=list(secret)
        # for i in range(len(guess)):
        #     if d[i]==guess[i]:
        #         a+=1
        #     if guess[i] in li:
        #         b+=1
        #         li.remove(guess[i])
        # b=b-a
        # return str(a)+'A'+str(b)+'B'
        # copy

        correct = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:  # 找到所有猜对的数的下标
                correct.add(i)
        a = len(correct)

        l1 = [0 for _ in range(10)]
        l2 = [0 for _ in range(10)]

        for i in range(len(secret)):
            if i not in correct:  # 跳过所有猜对的数
                l1[int(secret[i])] += 1  # li['1']=2
                l2[int(guess[i])] += 1

        b = sum([min(l1[i], l2[i]) for i in range(10)])  # 重合相加
        return str(a) + "A" + str(b) + "B"
        #
        # bull = sum(map(operator.eq, secret, guess))
        # sa = collections.Counter(secret)
        # sb = collections.Counter(guess)
        # cow = sum((sa & sb).values()) - bull
        # return str(bull) + 'A' + str(cow) + 'B'
        # copy2

