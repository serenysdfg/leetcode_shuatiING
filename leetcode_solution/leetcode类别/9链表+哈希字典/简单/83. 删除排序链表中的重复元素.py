# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # 遍历判断在不在set
        # if head == None or head.next == None:
        #     return head

        # pre = None
        # cur = head
        # while cur != None:
        #     pre = cur
        #     cur = cur.next
        #     while cur != None and cur.val == pre.val:
        #         pre.next = cur.next
        #         cur = cur.next

        # return head

        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next  # skip duplicated node #有排序
            head = head.next  # not duplicate of current node, move to next node
        return dummy
