class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        tmp = []

        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return mini
        
# minStack works by popping every element into another stack
# while trying to find the smallest value in the stack getting popped
# after value is found it is pushed back into the original stack