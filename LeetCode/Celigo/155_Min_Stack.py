class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1]>=val:
            self.min_stack.append(val)

    def pop(self) -> None:
        temp = self.stack[-1]
        self.stack = self.stack[:-1]
        if temp == self.min_stack[-1]:
            self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


a = ["MinStack","push","push","push","getMin","pop","top","getMin"]
b = [[],[-2],[0],[-3],[],[],[],[]]

obj = MinStack()

for i in range(1, len(a)):
    if a[i] == "push":
        obj.push(b[i][0])
    elif a[i] == "pop":
        obj.pop()
    elif a[i] == "top":
        print(obj.top())
    else:
        print(obj.getMin())