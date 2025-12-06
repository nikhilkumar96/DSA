from header import *
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.n =k

    def enQueue(self, value: int) -> bool:
        if len(self.queue)<self.n:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue =  self.queue[1:]
            return True
        return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return False if self.queue else True

    def isFull(self) -> bool:
        return True if len(self.queue)==self.n else False

a = ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
b = [[3],[1],[2],[3],[4],[],[],[],[4],[]]
obj = MyCircularQueue(b[0][0])

func_call_with_two_lists(a,b,obj)