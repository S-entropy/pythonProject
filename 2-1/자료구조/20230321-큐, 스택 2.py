''
class Queue():
   def __init__(self):
       self.in_stack = []
       self.out_stack = []

   def _transfer(self):
       while self.in_stack:
           self.out_stack.append(self.in_stack.pop())

   # _transfer를 사용한 경우 이후에 다시 원래의 in_stack에 돌려놓아야 함.
   def _revtransfer(self):
       while self.out_stack:
           self.in_stack.append(self.out_stack.pop())

   def enqueue(self, value):
       return self.in_stack.append(value)

   def dequeue(self):
       if not self.out_stack:
           self._transfer()
       if self.out_stack:
           v = self.out_stack.pop()
           self._revtransfer()
           return v
       else:
           print('Queue is empty')

   def size(self):
       return len(self.in_stack) + len(self.out_stack)

   def peek(self):
       if not self.out_stack:
           self._transfer()
       if self.out_stack:
           v = self.out_stack[-1]
           self._revtransfer()
           return v
       else:
           print('Queue is empty')
   # 먼저 dequeue되는 값을 앞에 두기 위해 새로 만든 코드
   def __str__(self):
       if not self.out_stack:
           self._transfer()
       if self.out_stack:
           ret = self.out_stack[:]
           ret.reverse()
           return str(ret)
       else:
           print('Queue is empty')

   def isEmpty(self):
       return not bool (len(self.in_stack)+len(self.out_stack))
q = Queue()
for i in range(10):
   q.enqueue(i)
for i in range(5):
   q.dequeue()
for i in range(10):
   q.enqueue(i)
print(q)
print(q.dequeue())
print(q)
print(q.size())
print(q.isEmpty())
print(q.peek())
'''
class Node:
   def __init__(self, value = None, pointer = None):
       self.value = value
       self.pointer = pointer

class LinkedQueue:
   def __init__(self):
       self.head = None
       self.tail = None
       self.count = 0

   def isEmpty(self):
       return not bool(self.count) # self.head도 가능

   def enqueue(self, value):
       newNode = Node(value)
       if not self.head:
           self.head = newNode
           self.tail = newNode
       else:
           if self.tail: # 없어도 상관X
               self.tail.pointer = newNode
           self.tail = newNode
       self.count+=1

   def dequeue(self):
       if self.head:
           value = self.head.value
           self.head = self.head.pointer
           self.count-=1
           # self.count가 이 시점에서 0이 된다면 head = tail이었던 것이다.
           if self.count == 0:
               self.tail = None
           return value
       else:
           raise Exception('Queue is empty')

   def size(self):
       return self.count

   def peek(self):
       # Queue가 비어있는 경우에 대한 오류 수정
       if self.count:
           return self.head.value
       else:
           raise Exception('Queue is empty')

   def print(self):
       node = self.head
       while node:
           print(node.value, end=' ')
           node = node.pointer
       print()
q = LinkedQueue()
for i in range(10):
   q.enqueue(i)
for i in range(5):
   q.dequeue()
for i in range(10):
   q.enqueue(i)
q.print()
print(q.dequeue())
q.print()
print(q.size())
print(q.isEmpty())
print(q.peek())

# 
Queue1.py
class Queue(object):
   def __init__(self):
       self.items = []

   def isEmpty(self):
       return not bool(self.items)

   def enqueue(self, value):
       self.items = [value] + self.items

   def dequeue(self):
       if len(self.items):
           val = self.items[-1]
           self.items = self.items[:-1]
           return val
       else:
           print('Stack is Emapy\n')

   def size(self):
       return len(self.items)

   def peek(self):
       if self.items:
           return self.items[-1]
       else:
           print('Stack is Empty\n')


Dequeue1.py
from Queue1 import Queue
class Deque(Queue):
   def enqueue_back(self, item):
       self.items.append(item)
   def dequeue_front(self):
       value = self.items.pop(0)
       if value is not None:
           return value
       else:
           print('Deque is empty')

if __name__ == '__main__':
   dq = Deque()
   print(dq.isEmpty())
   for i in range(5):
       dq.enqueue(i)
   for i in range(5):
       dq.enqueue_back(i)
   print(dq.dequeue())
   print(dq.items)
   print(dq.dequeue_front())
   print(dq.items)
