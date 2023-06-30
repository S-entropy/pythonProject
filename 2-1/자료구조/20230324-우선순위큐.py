import random
# 우선순위 큐 만들기
class pq(object):
   def __init__(self, enumlist):
       self.pq = enumlist
       random.shuffle(self.pq)
       self.cnt=0
   def print(self):
       print(self.pq)
   def deque(self):
       for i in self.pq:
           a, b = i
           if a == self.cnt:
               self.cnt+=1
               return i
mylist = ['a', 'b', 'c', 'd', 'e']
list = list(enumerate(mylist))
random.shuffle(list)
q = pq(list)
q.print()
for i in range(5):
   print(q.deque())


#나머지 코드
#Deque의 단점
#삽입, 삭제시 비효율적(리스트)
#파이썬에서 제공하는 큐를 사용하면 됨.
#collections 패키지의 deque 모듈
#deque는 양쪽 방향에서 삽입, 삭제 가능
#deque(maxlen = 4)
from collections import deque
q = deque(['kim', 'lee', 'park'])
q.append('y')
q.appendleft('c')
print(q)
q.pop()
print(q)
q.popleft()
print(q)
q.rotate(1)
print(q)
q.rotate(-1)
print(q)

#enumerate 함수 : built-in function
i = 0
for ch in ['a','b','c']:
   print(i, ch)
   i+=1
for ch in enumerate(['a', 'b', 'c']):
   print(ch)
for i, ch in enumerate(['a', 'b', 'c']):
   print(i, ch)
mylist = ['a','b','c']
i = iter(mylist)
print(next(i))
print(next(i))
print(next(i))
i = enumerate(mylist)
print(next(i))
print(next(i))
print(next(i))
matrix = [['a','b','c'],
         ['d','e','f'],
         ['g','h','i']]
for i, row in enumerate(matrix):
   for j, ch in enumerate(row):
       print(i, j, ch)

