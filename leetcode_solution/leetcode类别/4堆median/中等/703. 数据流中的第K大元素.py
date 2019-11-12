设计一个找到数据流中第K大元素的类（

class ）。注意是排序后的第K大元素，不是第K个不同的元素。


你的 KthLargest 类需要一个同时接收整数 k
和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int
k = 3;
int[]
arr = [4, 5, 8, 2];
KthLargest
kthLargest = new
KthLargest(3, arr);
kthLargest.add(3);    // returns
4
kthLargest.add(5);    // returns
5
kthLargest.add(10);  // returns
5
kthLargest.add(9);    // returns
8
kthLargest.add(4);    // returns
8

from heapq import *
class KthLargest:

    # copy
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # 只保留最大的k个，可以弹出时就是第k大

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:  # nums初始个数没有=k-1时候，特殊情况
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# heapq.heappush(heap, item): 将 item 的值加入 heap 中，保持堆的不变性。
# heapq.heappop(heap):弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。
# heapq.heappushpop(heap, item):将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。
# heapq.heapify(x): 将list x 转换成堆，原地，线性时间内。
# heapq.heapreplace(heap, item):弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。