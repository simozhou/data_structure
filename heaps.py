class MinHeap(object):
    """ We will use AREIS to implement our heap.
    We know that each consecutive node is 2-fold away from the node you're starting so we can work by indexes"""

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        """to re-balance the heap every time we update the structure (i.e. deletion, insertion)"""
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    @property
    def delMin(self):
        retval = self.heapList[1]
        # we put on top the last element in order let everything rebalance properly
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

