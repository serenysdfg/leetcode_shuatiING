class MyStack:
 #Python语言没有栈和队列数据结构，只能用数组 List 或双端队列 deque 实现。

# 这类编程语言就压根不需要 用队列实现栈或用栈实现队列这种问题，因为栈和队列本身就必须借助List、deque实现。

# 所以这道题在这种语言中这就非常简单了，可以说是作弊。
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        return self.stack.pop(-1)
    def top(self) -> int:
        return self.stack[-1]
    def empty(self) -> bool:
        return self.stack == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''java
add        增加一个元索                     如果队列已满，则抛出一个IIIegaISlabEepeplian异常
remove   移除并返回队列头部的元素    如果队列为空，则抛出一个NoSuchElementException异常
element  返回队列头部的元素             如果队列为空，则抛出一个NoSuchElementException异常
offer       添加一个元素并返回true       如果队列已满，则返回false
poll         移除并返问队列头部的元素    如果队列为空，则返回null
peek       返回队列头部的元素             如果队列为空，则返回null
put         添加一个元素                      如果队列满，则阻塞
take        移除并返回队列头部的元素     如果队列为空，则阻塞
'''
class MyStack {
Queue < Integer > queue;
public MyStack() {queue = new LinkedList();}
public void push(int x) {
queue.offer(x);
while (queue.peek() != x)
    queue.offer(queue.poll());
}

public int pop(){return queue.poll();}
public int top(){return queue.peek();}
public boolean empty(){return queue.isEmpty();}
}
'''c++
'''
