class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        self.end = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)    
        self.end = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))          
        answer = self.q1.pop(0)
        while len(self.q2) > 0:
            self.q1.append(self.q2.pop(0))
        self.end = self.q1[len(self.q1)-1] if len(self.q1) > 0 else None
        return answer

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.end

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0