class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.arr = [None]*k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.arr[self.rear] = value
            else:
                self.arr[(self.rear + 1)%self.k] = value
                self.rear = (self.rear + 1)%self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.arr[self.front] = None
            else:
                self.arr[self.front] = None
                self.front = (self.front + 1)%self.k
            return True

    def Front(self) -> int:
        return self.arr[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.arr[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.arr[self.front] is None

    def isFull(self) -> bool:
        return (self.rear + 1)%self.k == self.front if self.k > 1 else self.arr[self.front] != None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
