class Solution:
    def reverseVowels(self, s: str) -> str:
    #     # #看个数--自己写
    #     count=(s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')+s.count('A')+s.count('E')+s.count('I')+s.count('O')+s.count('U'))//2
    #     i=0
    #     s=list(s)
    #     start,end=0,len(s)-1
    #     while i<count: #直接start《end就可以
    #         while s[start] not in ['a','e','i','o','u','A','E','I','O','U']:
    #             start+=1
    #         while s[end] not in ['a','e','i','o','u','A','E','I','O','U']:
    #             end-=1
    #         s[end], s[start]  = s[start],s[end]#互换
    #         start+=1 #hu
    #         end-=1
    #         i+=1
    #     return ''.join(s)   
    # #copy1正则
    # vowels = re.findall('(?i)[aeiou]', s)
    # return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
    # #copy2  ok
    #     vowels = 'aeiou'
    #     string = list(s)
    #     i, j = 0, len(s) -1
    #     while i <= j:
    #         if string[i].lower() not in vowels:
    #             i += 1
    #         elif string[j].lower() not in vowels:
    #             j -= 1
    #         else:
    #             string[i], string[j] = string[j], string[i]
    #             i += 1
    #             j -= 1
    #     return ''.join(string)
    #copy3
        vowels = set(['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O'])
        p = [i for i in s if i in vowels] #去除元音
        return ''.join([i if i not in vowels else p.pop() for i in s]) #后面的先吐出来