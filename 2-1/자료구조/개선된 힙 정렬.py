import heapq
import math
def heapSort(x):
    heapq.heapify(x)
    l = []
    while len(x):
        l.append(heapq.heappop(x))
    return l
def insertSort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j+1]  = x[j]
            j = j - 1
        x[j+1] = key
    return x

def goodSort(x):
    v = len(x)-1
    cnt = 0
    prev = None
    cur = x[0]
    for i in range(1, v+1):
        prev = cur
        cur = x[i]
        if prev>cur:
            cnt+=1
    if cnt<math.log(v, 2):
        return insertSort(x)
    else:
        return heapSort(x)
l = [9,8,7,6,5,4,3,2,1]
l = goodSort(l)
print(l)