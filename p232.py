class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)
        print(self.s1)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        value = self.s2.pop()
        self.front = self.s2[-1] if len(self.s2) > 0 else None
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())        
        print(self.s1)
        return value    

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0