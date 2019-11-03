class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #1未运行   
        order = [1001] * 1001
        for i, c in enumerate(arr2):
            order[c] = i

        for i, c in enumerate(order):
            if c == 1001:
                order[i] = i + 1000
        return sorted(arr1, key=lambda a : order[a]
                #2简单写法
        order = {v: i for i, v in enumerate(arr2)} #{字符：顺序}
        return sorted(arr1 , key=lambda a: order.get(a, 1000 + a)) #通过index+1000的方式指定其优先级（其中index表示元素在arr1中的位置）。key
    