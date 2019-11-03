class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # copy
        # 需要一个栈来储存暂时没有遇到其更大元素的数。然后遍历nums2
        # 如果遇到的数比栈中的某些元素大，则其为那些元素的下个更大数，然后将那些元素从栈中移除，存入哈希表中，并把最新遇到的数放入栈中
        # nums1 = [4,1,2], nums2 = [1,3,4,2]，遍历 nums2，第一个数是1，放入栈中(stack = [1])。第二个元素是3，比1大，将1从栈中移除，把(1, 3)存入哈希表中，并把3放入栈中(stack = [3]， hash_map = { 1:3 })。对第三个数4进行相同的操作(stack = [4]， hash_map = { 1:3, 3:4 })
        dic, stack = {}, []  # dict(), list()
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)
        return [dic.get(i, -1) for i in nums1]  # default -- 如果指定键的值不存在时，返回该默认值
