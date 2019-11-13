"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #copy未看
        res = []                                                # 结果列表
        queue = [root]                                          # 当前层的结点

        while queue:                                            # 当前层存在结点时
            cur_layer = []                                      # 初始化当前层结果列表为空
            next_queue = []                                     # 初始化下一层结点列表为空

            for node in queue:                                  # 遍历当前层的每一个结点
                if node:                                        # 如果该结点不为空，则进行记录
                    cur_layer.append(node.val)                  # 将该结点的值加入当前层结果列表的末尾
                    next_queue.extend(node.children)            # 将该结点的孩子结点加入到下一层结点列表

            if cur_layer:                                       # 只要当前层结果列表不为空
                res.insert(0, cur_layer)                        # 则把当前层结果列表加入到结果列表首端
            queue = next_queue                                  # 更新当前层节点列表为下一层结点列表

        return res                                              # 返回最终结果