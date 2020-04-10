class CustomStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if (self.is_empty()):
            return -1
        else:
            return self.stack.pop()

    def push(self, item):
        return self.stack.append(item)

    def top(self):
        if(self.is_empty()):
            return -1
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)