class MyQueue:

    def __init__(self):
        self.stack=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        a=self.stack[0]
        del self.stack[0]
        return a
    def peek(self) -> int:
        return self.stack[0]
    def empty(self) -> bool:
        return self.stack == []
