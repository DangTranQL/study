from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None
    def size(self):
        return len(self.stack)
    def empty(self):
        return True if self.size() == 0 else False
    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]
