'''以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        #copy
        stack = list()
        path = [p for p in path.split('/') if p]
        for f in path:
            if f == '.': 
                continue#不管
            elif f == '..': 
                if stack: 
                    stack.pop()
            else: 
                stack.append(f)##要经常添加删除的用栈

        return '/'+'/'.join(stack)