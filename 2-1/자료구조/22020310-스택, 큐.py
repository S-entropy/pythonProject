학번 2202      이름 김기범

'''
# Queue 구현
# FIFO 구조
# 배열의 인덱스 접근은 제한
class Queue(object):
   def __init__(self):
       self.items = []
   def isEmpty(self):
       return not bool(self.items)

   def enqueue(self, value):
       self.items.insert(0, value)

   def dequeue(self):
       value = self.items.pop()
       if value is not None:
           return value
       else:
           print('Queue is empty')

   def size(self):
       return len(self.items)
   def peek(self):
       if self.items:
           return self.items[-1]
       else:
           print('Queue is empty')

q = Queue()
#print(q.isEmpty())
#print(f'size : {q.size()}')
for i in range(10):
   q.enqueue(i)
while not q.isEmpty():
   v = q.dequeue()
   print(v)
# list function
# list.append(x) : x값을 뒤에 추가
# list.insert(index,x) : index가 범위를 넘어가면 그냥 맨 뒤에 붙음
# list.remove(x) : 특정 값을 찾아 제거
# list.pop() : 리스트의 마지막 값을 반환 후 사제
# list.extend(list2) : 리스트를 서로 연결
# list.count(x) : 값 x의 개수
# list.index(x) : 값 x의 index
# list.sort()
# list.reverse()
'''
from collections import deque
q = deque([1,2,3])
q.append(4)
q.appendleft(0)
print(q)
print(q.pop())
q = deque([1,2,3])
for i in range(7,10):
   q.append(i)
print(q)

