class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a)-1

    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self):
        if self.N==0:
            print('Heap is Empty')
            return None
        mininum = self.a[1]
        self.a[1], self.a[-1]=self.a[-1], self.a[1]
        del self.a[-1]
        self.N-=1
        self.downheap(1)
        return mininum

    def downheap(self, i):
        while 2*i<=self.N:
            k = 2*i
            if k<self.N and self.a[k] > self.a[k+1]:
                k+=1
            if self.a[i] < self.a[k]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i=k

    def upheap(self, j):
        while j>1 and self.a[j//2]>self.a[j]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.a[i], self.a[i], ']', end='')
        print('\n힙 크기 = ', self.N)
def find_minimum_value(arr) :
    b = BHeap(arr)
    b.create_heap()
    return b.a[1]


