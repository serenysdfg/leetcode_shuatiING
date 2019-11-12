'''输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-compression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        # 从后向前遍历，这样在压缩的时候就不用更新索引
        count = 1
        length = len(chars)

        for index in range(length - 1, -1, -1):
            if index > 0 and chars[index] == chars[index - 1]:
                count += 1
            else:
                end = index + count
                if count == 1:
                    chars[index:end] = [chars[index]]
                else:
                    chars[index:end] = [chars[index]] + list(str(count))
                    count = 1

        return len(chars)
        # 遍历数组，用flag记录当前计数的字符，num表示当前计数字符的个数，index表示当前字符的索引，i表示数组的索引
        # 如果当前字符与flag相同，num加1
        # 如果不同，分三种情况：
        # 1.num=0：表示是第一个字符，令index=0
        # 2.num=1：表示当前计数的字符只有一个，不用添加数字替换，令index加1即可
        # 3.num大于等于1：表示计数的字符多于两个，需要用字符形式的数字替换多余的字符
        # 同时更新index以及i的值
#         flag=''#当前字符
#         num=0#当前字符个数
#         index=0#字符索引
#         chars.append('ll')
#         i=0
#         while flag!='ll':
#             if chars[i]==flag:
#                 num+=1
#             else:
#                 if num==0:
#                     index=0
#                 elif num!=1:
#                     chars[index+1:index+num]=[j for j in str(num)]#把字母用字符形式数字替换
#                     index+=len(str(num))+1
#                     i=index
#                     #print(chars)
#                 else:
#                     index+=1
#                 flag=chars[i]
#                 num=1 

#             i+=1
#         chars=chars[:-1]
#         return len(chars)


# 超时间，错误一个不用替代
# n=len(chars)
# dict={}
# i=0
# while i <n-1:
#     dict[chars[i]]=1
#     while  chars[i]==chars[i+1]:
#         dict[chars[i]]=dict.get( chars[i],0)+1
#     i+=1
# if chars[n-2]!=chars[n-1]:
#     dict[chars[n-1]]=1
# return len(''.join(str(i) for i in list(dict.values())))+len(dict)