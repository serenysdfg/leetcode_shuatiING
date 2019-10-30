#
# @lc app=leetcode.cn id=192 lang=bash
#
# [192] 统计词频
#
# https://leetcode-cn.com/problems/word-frequency/description/
#
# shell
# Medium (27.01%)
# Total Accepted:    2.3K
# Total Submissions: 8.5K
# Testcase Example:  'a'
#
# 写一个 bash 脚本以统计一个文本文件 words.txt 中每个单词出现的频率。
# 
# 为了简单起见，你可以假设：
# 
# 
# words.txt只包括小写字母和 ' ' 。
# 每个单词只由小写字母组成。
# 单词间由一个或多个空格字符分隔。
# 
# 
# 示例:
# 
# 假设 words.txt 内容如下：
# 
# the day is sunny the the
# the sunny is is
# 
# 
# 你的脚本应当输出（以词频降序排列）：
# 
# the 4
# is 3
# sunny 2
# day 1
# 
# 
# 说明:
# 
# 
# 不要担心词频相同的单词的排序问题，每个单词出现的频率都是唯一的。
# 你可以使用一行 Unix pipes 实现吗？
# 
# 
#
# Read from the file words.txt and output the word frequency list to stdout.
# 算法思路其实挺简单的: 先分割字符串, 然后使用一个dict来存储相应的计数, 再基于计数进行倒序排列, 最后输出对应的单词和计数即可.

# 现在重点是怎么使用bash脚本完成这个算法过程了~~~

# grep 查找
# [[:alpha:]]表示字母
# grep -E -o "\b[[:alpha:]]+\b" 匹配出所有的单词
# count[XXX] 为shell中的字典
# awk BEGIN 为处理文件之前的操作, 而END 为处理文件之后的操作, 不匹配任何行, 常用语输出一些总结信息
grep -E -o "\b[[:alpha:]]+\b" words.txt | awk ' { count[$0]++ }
END{
for(word in count)
{printf("%s %s\n",word,count[word])}
}' | sort -k2nr

