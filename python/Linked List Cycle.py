class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        tmp = ListNode(0)
        result  = False
        if head == None:
            return(result)
        while head:
            if head.next == None:
                return(result)
            if head.next == tmp: #
                result = True
                return(result)
            cur, head.next = head.next, tmp
            head = cur

'''与上个题类似，只不过不是判断是否有循环，变为了如果有循环则输出循环开始的位置，这个题就不能向上一个题那样做了，因为上一个题改变了原有的链表的结构，而这个题要返回链表，所有不幸，但思路一致，我们可以把遍历过的节点的值都变为负无穷，如果遇到节点的信息为负无穷，那么这个点就是循环开始的点。代码如下：'''

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    class Solution:
        # @param head, a ListNode
        # @return a list node
        def detectCycle(self, head):
            if head == None:
                return(None)
            while head:
                if head.next == None:
                    return(None)
                if head.val == float("inf"):
                    return(head)
                head.val = float("inf")
                head = head.next