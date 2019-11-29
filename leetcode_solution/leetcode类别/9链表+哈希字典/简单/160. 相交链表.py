# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
            #https://blog.csdn.net/qq_34364995/article/details/80518198
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        pA = headA
        pB = headB
        #获取长度
        while pA:
            pA = pA.next
            lenA += 1
        while pB:
            pB = pB.next
            lenB += 1
        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                pA = pA.next
        else:
            for i in range(lenB-lenA):
                pB = pB.next
        while pA!=pB:
            pA = pA.next
            pB = pB.next
        return pA

#         '''        思路是这样的（题目中假设没有环）：
# 1.分别遍历两个链表，如果尾节点不同则不相交，返回None，如果尾节点相同则求相交结点。
# 2.求相交结点的方法是，求出链表长度的差值，长链表的指针先想后移动lenA-lenB。然后两个链表一起往后走，若结点相同则第一个相交点。
# 3.求链表的长度，在遍历的时候就计算，并将每个结点放在字典中。
# 该题中不让修改链表结构。所以只考虑以上思路。还有另一种方法是：
# 先遍历第一个链表到他的尾部，然后将尾部的next指针指向第二个链表(尾部指针的next本来指向的是null)。这样两个链表就合成了一个链表，判断原来的两个链表是否相交也就转变成了判断新的链表是否有环的问题了：即判断单链表是否有环？

# '''
#用字典
        a = headA
        b = headB
        da = {0:a}
        db = {0:b}
        i = 0
        l = m =0
        while a:
            a = a.next
            l += 1
            da[l] = a
        while b:
            b = b.next
            m += 1
            db[m]  = b
        if db[m] != da[l]:
            return None
        i = 0
        if l >= m:
            diff = l - m
            while True:
                if da[i]==db[diff]:
                    return da[i]
                diff+=1
                i+=1
        if l < m:
            diff = m - l
            while True:
                if db[i] == da[diff]:
                    return db[i]
                diff+=1
                i+=1



#         #比较巧妙的数学解法，看下面的解释和代码:线段重合就是交点
#         pA, pB = headA, headB
#         while pA is not pB:
#             pA = pA.next if pA else headB
#             pB = pB.next if pB else headA
#         return pA
#         #查看哪个相等,一个一个O(N2)
#         #lose
#         # p=headB
#         # while headA :
#         #     headB=p
#         #     while headB :
#         #         print(headA.val)
#         #         print(headB.val)
#         #         if headA.val==headB.val:return headB.val
#         #         else:
#         #             headB=headB.next
#         #     headA=headA.next
#         # return null