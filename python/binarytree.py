class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        return(self.preorderTraversal1(root, result))
    def preorderTraversal1(self, root, result):
        if root == None:
            return(result)
        result.append(root.val)
        if root.left:
            result = self.preorderTraversal1(root.left, result)
        if root.right:
            result = self.preorderTraversal1(root.right, result)
        return(result)
#后序遍历把result.append(root.val)放在后面，中序变化位置