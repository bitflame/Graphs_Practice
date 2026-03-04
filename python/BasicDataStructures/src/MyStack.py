class MyStack:
    def __init__(self):
        self.__values = []

    def push(self, val):
        self.__values.append(val)

    def pop(self):
        if self.is_empty():
            raise StackIsEmptyException()
        return self.__values.pop()

    def peek(self):
        if self.is_empty():
            raise StackIsEmptyException()
        return self.__values[ - 1]

    def is_empty(self):
        return len(self.__values) == 0

class StackIsEmptyException(Exception):
    pass

stack = MyStack()
stack.push("first")
stack.push("second")
print("should be second: ", stack.peek())
print("should be second: ", stack.pop())
print("should be first: ", stack.pop())
print("should be True: ", stack.is_empty())
