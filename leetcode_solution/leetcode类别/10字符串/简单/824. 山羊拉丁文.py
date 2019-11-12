class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        A = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(words)
        for i in range(n):
            if words[i][0] in A:
                words[i] = words[i] + 'ma' + 'a' * (i + 1)
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma' + 'a' * (i + 1)

        return ' '.join(i for i in words)