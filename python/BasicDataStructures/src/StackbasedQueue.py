from python.BasicDataStructures.src.MyQueue import QueueIsEmptyException
from python.BasicDataStructures.src.MyStack import MyStack


class Stacki_Queue:
    def __init__(self):
        self._inbox = MyStack()
        self._outbox = MyStack()

    def enqueue(self, elem):
        self._inbox.push(elem)

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmptyException()
        self.transfer_inbox_to_outbox()
        return self._outbox.pop()

    def peek(self):
        if self.is_empty():
            raise QueueIsEmptyException
        self.transfer_inbox_to_outbox()
        return self._outbox.peek()

    def is_empty(self):
        return self._inbox.is_empty() and self._outbox.is_empty()

    def _transfer_inbox_to_outbox(self):
        if self._outbox.is_empty():
            while not self._inbox.is_empty():
                self._outbox.push(self._inbox.pop())
