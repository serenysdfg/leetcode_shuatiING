# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #copy双指针ok
        fast = slow = head
        # 找到中间节点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 翻转后半部分
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # 比较前后两部分
        while prev: # while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        # # copy数组
        # vals = []
        # while head:
        #     vals += head.val,
        #     head = head.next
        # return vals == vals[::-1]