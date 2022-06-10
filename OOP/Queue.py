from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        try:
            return self.queue.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None
    def size(self):
        return len(self.queue)
    def display(self):
        print(self.queue)
    def contains(self, data):
        return data in self.queue
    def iter(self):
        yield from self.queue
    def reversed(self):
        yield from reversed(self.queue)