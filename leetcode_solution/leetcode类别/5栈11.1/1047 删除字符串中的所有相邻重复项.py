class Solution:
    def removeDuplicates(self, S: str) -> str:
        #me
        stack=[]
        for n in S:
            if stack and stack[-1]==n:
                stack.pop()
            else:
                stack.append(n)
        return "".join(stack)