class Queue(object):
    """FIFO data structure"""
    def __init__(self, size):
        self.body = []
        self.size = size

    def getSize(self):
        return self.size

    def enqueue(self, value):
        self.body.append(value)
        self.size += 1
        print("Enqueued:", value)

    def dequeue(self):
        val = self.body.pop(0)
        self.size -= 1
        print("Dequeued value:", val)
        return val

    def peek(self):
        return self.body[0]


if __name__ == '__main__':

    d = Queue(1)
    for i in range(1,11):
        d.enqueue(i)

    print('First element:',d.peek())

    for i in range(1,11):
        print(d.dequeue())

