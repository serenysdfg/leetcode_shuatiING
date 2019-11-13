# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #超时，自己写
#         if head==None :return False
#         while head.next!=None and head.next.val!=head.next.val-1:
#             head.val-=1
#             head=head.next
#         if head.next==null :
#             return False
#         else:
#             return True
        #copy追赶，双指针
#         if head == None:
#             return False
        
#         fast, slow = head, head
#         while fast.next != None and fast.next.next != None:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True

#         return False
    #copy2字典记录放入kkey  时间，空间复杂度都是O（n）
        if head == None: return False
        dictx = {}
        cur = head
        while cur:
            if cur in dictx:
                return True
            dictx[cur] = 1
            cur = cur.next
        return False