设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []                         # 定义一个基本栈，用于存储每个元素
        self.min = []                           # 定义一个最小栈，其栈顶元素是当前基本栈中的最小值

    def push(self, x: int) -> None:
        self.stack.append(x)                    # 把元素压入栈中
        if not self.min or x < self.min[-1]:    # 如果最小栈为空或新元素比基本栈的最小值还要小
            self.min.append(x)                  # 该元素是目前出现的最小值，压入最小栈
        else:                                   # 否则
            self.min.append(self.min[-1])       # 将最小栈中的栈顶元素复制一遍压入最小栈,表示这时候最小是这个

    def pop(self) -> None:
        self.min.pop()                          # 弹出最小栈中的元素，保证两个栈元素个数相同
        return self.stack.pop()                 # 弹出基本栈中的元素

    def top(self) -> int:
        return self.stack[-1]                   # 返回基本栈的栈顶元素
    def getMin(self) -> int:
        return self.min[-1]                     # 返回最小栈的栈顶元素



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()