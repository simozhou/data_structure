import sys

class StackError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self):
        return "%s: %s" % (self.expression, self.message)


class Stack(object):

    def __init__(self, size):
        self.content = []
        self.size = size
        self.min = [sys.maxsize]

    def mySize(self):
        return self.size

    def isEmpty(self):
        return not bool(self.content)

    def push(self, value):
        if self.mySize() > self.size:
            raise StackError("Stack is full", "can't do anything")
        if self.isEmpty():
            self.min.insert(0, value)
        else:
            if value < self.min[0]:
                self.min.insert(0, value)
            else:
                self.min.insert(0,self.min[0])
            self.content.insert(0, value)

    def pop(self):
        value = self.content.pop(0)
        self.min.pop(0)
        return value

    def minimum(self):
        val = sys.maxsize
        for i in self.content:
            if val > i:
                val = i
        return val

if __name__ == '__main__':

    q = Stack(5)
    try:
        for i in range(0,7):
            q.push(i)
    except StackError as e:
        print("messed up >>>", e)

    finally:
        print(q.minimum(), q.min)