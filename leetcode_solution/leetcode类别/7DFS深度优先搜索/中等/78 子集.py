#https://blog.csdn.net/qq_17550379/article/details/82621887
#递归，DFS，数组，位运算
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #递归-只要知道了subsets(nums[1:])，那么我们只要将nums[0]添加到每个子集的前面形成新的子集，然后将新的子集添加到result中即可
        if not nums:
            return [[]]
        result = self.subsets(nums[1:]) #
        return result + [[nums[0]] + s for s in result]
        # copy1
        # 每次拿一个，跟res里面的每一个已有列表取并集再次插入res中
        # res = [[]]
        # for num in nums:
        #     res.extend([tmp+[num] for tmp in res])
        # return res 

        # nums.sort()
        # res = []
        # 对每个元素，有两种可能，加入 cur_lst 和不加入 cur_lst，写起来思路还是很清爽的
        # nums.sort()
        # res = []

        # def search(cur_lst, idx):
        #     if idx == len(nums):
        #         res.append(cur_lst)
        #         return
        #     search(cur_lst + [nums[idx]], idx + 1)
        #     search(cur_lst, idx + 1)

        # search([], 0)
        # return res

        # DFS
        nums.sort()
        res = []

        def dfs(depth, start, lst):
            res.append(lst)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, lst + [nums[i]])

        dfs(0, 0, [])
        return res

        # 5
        list2 = []
        for i in range(len(nums) + 1):
            list1 = list(itertools.combinations(nums, i))
            list2.extend(list1)
        list1 = []
        list2 = list(set(list2))
        for i in list2:
            list1.append(list(i))
        return list1
        # 自己lose
        # n=len(nums) 
        # a=[[]]
        # for i in range(n):#先加入第几个
        #     a.append([nums[i]])
        #     a1=[nums[i]]
        #     for j in range(i+1,n)):#
        #         for k in range(n):#长度n
        #             a1.append(nums[j])
        # a=[]
        # a.append(path)