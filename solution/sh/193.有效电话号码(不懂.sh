#
# @lc app=leetcode.cn id=193 lang=bash
#
# [193] 有效电话号码
#
# https://leetcode-cn.com/problems/valid-phone-numbers/description/
#
# shell
# Easy (22.60%)
# Total Accepted:    2.4K
# Total Submissions: 10.8K
# Testcase Example:  '0'
#
# 给定一个包含电话号码列表（一行一个电话号码）的文本文件 file.txt，写一个 bash 脚本输出所有有效的电话号码。
# 
# 你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）
# 
# 你也可以假设每行前后没有多余的空格字符。
# 
# 示例:
# 
# 假设 file.txt 内容如下：
# 
# 987-123-4567
# 123 456 7890
# (123) 456-7890
# 
# 
# 你的脚本应当输出下列有效的电话号码：
# 
# 987-123-4567
# (123) 456-7890
# 
# 
#
# Read from the file file.txt and output all valid phone numbers to stdout.

# 题目中提到了两种形式:

# (xxx) xxx-xxxx对应\(\d{3}\) \d{3}-\d{4}
# xxx-xxx-xxxx对应\d{3}-\d{3}-\d{4}
# 合在一起表达为: /^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}/, 前面使用awk.

# 而前面为grep时, 脚本为:^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}, 前面使用grep.
awk '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/' file.txt
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt