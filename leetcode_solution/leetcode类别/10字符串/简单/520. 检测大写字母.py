'''
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-capital
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 和ascii对比  2islower后和原来相同
        if len(word) == 1: return True
        if len(word) == 2:
            if word[0].islower() and word[1].isupper():
                return False
            else:
                return True
        if word[0].islower():  # 首字母小写
            if word.lower() != word:
                return False
        elif word[1].islower():  # 只有首字母大写
            if word[1:].lower() != word[1:]: return False
        else:  # 第二个也是大写
            if word.upper() != word: return False

        return True
        # copy
        sum1 = 0
        for i in word:
            if i == i.upper():
                sum1 += 1

        if sum1 == len(word) or (sum1 == 1 and word[0] == word[0].upper()) or sum1 == 0:  # 三种情况 #大写个数0或者 1或者全部
            return True
        else:
            return False
