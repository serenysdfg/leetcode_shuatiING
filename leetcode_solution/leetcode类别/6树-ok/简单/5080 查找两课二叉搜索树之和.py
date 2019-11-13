'''
给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。

如果可以找到返回 True，否则返回 False。
'''
'''
注释：先中序遍历，就会把元素按照顺序存在容器中了，再两个for循环

思路一
一个非常简单的方案是，将其中一棵树放入哈希表中，再依次遍历另一颗树，对于每个元素检测其补值（Target - curNum）是否存在哈希表中。

此时时间复杂度为O(min
{ | M |, | N |})。（ | M |， | N | 分别为两棵树的大小）。

但这个方案需要使用哈希表，显然复杂度的常数较大，并且对空间也有一定的要求。

思路二
使用中序遍历将两棵树的元素分别保存（升序），使用双指针分别指向两个列表的头、尾。

此时可以借鉴文章开头提到的题目思路，不断移动双指针即可。

时间复杂度与空间复杂度均为O( | M | + | N |)。（暂未考虑中序遍历时的递归空间需求）

实现
思路一比较简单，思路二的实现如下：
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorder(node: TreeNode, li: list):
    if node == None:
        return
    inorder(node.left, li)
    li.append(node.val)
    inorder(node.right, li)


class Solution:
    #没仔细看
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        li_1, li_2 = [], []
        inorder(root1, li_1)
        inorder(root2, li_2)
        p1, p2, len1 = 0, len(li_2) - 1, len(li_1) #双指针分别指向两个列表的头、尾。

        while p1 < len1 and p2 >= 0:
            judge = li_1[p1] + li_2[p2] - target
            if judge == 0:
                return True
            elif judge > 0:
                p2 -= 1
            else:
                p1 += 1
        return False