'''
print([False] * 5)
print([False] for _ in range(5))
print([ [False] for _ in range(5)])
print('*'  *  30)

print([0]*5)
print([0 for _ in range(5)])
print([0] for _ in range(5))
print([[0] for _ in range(5)])
print('*' * 30)

n = 4
graph = [ [ 0 for j in range(n) ] for i in range(n) ]
print(graph)
graph = [ [0] * 4 for _ in range(4)]
print(graph)
graph = [ '0' * 4 for _ in range(4)]
print(graph)
n, a, d = map(int,input().split())
ans = []
for i in range(n):
    ans.append(a)
    a*=d
print(ans)
from itertools import permutations
def string_permutations(s):
    perms = permutations(s) # <class 'itertools.permutations'> 안에 tuple
    sorted_perms = sorted([''.join(p) for p in perms])
    return sorted_perms


# 예제 입력 및 출력
input_str = "abc"
print(string_permutations(input_str))
from itertools import permutations
def string_permutations(s, d):
    perms = permutations(s)
    sorted_perms = sorted([int(''.join(p)) for p in perms])
    larger = [i for i in sorted_perms if i >d]
    larger.sort()
    return larger
*l, d = map(int,input().replace('[','').replace(']','').split(','))
l = list(map(str,l))
P = permutations(l)
larger = []
for i in P:
    v = list(i)
    v = ''.join(v)
    v = int(v)
    if v>d:
        larger.append(v)
larger.sort()
if len(larger):
    print(larger[0])
else:
    print(-1)
larger = string_permutations(l,d)
if len(larger):
    print(larger[0])
else:
    print(-1)
numlist = input().replace('[', '').replace(']','').split(',')
print(numlist)
def is_palindrome(l):
    l = l.replace(' ', '')
    revl = l[::-1]
    # return l == revl
    for i in range(len(l)):
        if l[i]!=revl[i]:
            return False
    return True
    print(l, revl)
l = input()
print(is_palindrome(l))
import time
def list_pop():
  n = int(input())
  lst = [1] * n


  s = time.time()
  print(f'시작 : {s}')
  while lst:
    lst.pop(0)
  e = time.time()
  print(f'끝 : {e}')


  interval = e - s
  print(str(n) + ':' + str(interval))
from queue import Queue
def queue_pop():
  n = int(input())
  q = Queue()
  for i in range(n):
    q.put(i) #q.put(i, 1)


  s = time.time()
  print(f'시작 : {s}')
  while not q.empty():
    q.get()
  e = time.time()
  print(f'끝 : {e}')


  interval = e - s
  print(str(n) + ':' + str(interval))
import time
from collections import deque
def deque_pop():
  n = int(input())
  dq = deque([1] * n)


  s = time.time()
  print(f'시작 : {s}')
  while dq: # 'collections.deque' object has no attribute 'empty'
    dq.popleft()
  e = time.time()
  print(f'끝 : {e}')


  interval = e - s
  print(str(n) + ':' + str(interval))


list_pop()
queue_pop()
deque_pop()
'''
# 개선된 버블정렬
def bubbleSort(x):
    length = len(x)-1
    eidx = length
    for i in range(length):
        exchange= False
        last = length
        for j in range(eidx):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                last=j
                exchange = True
        eidx = last
        if not exchange:
            break
    return x
list = [5,4,3,2,1,0]
print(bubbleSort(list))