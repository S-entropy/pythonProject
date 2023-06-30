class Node:
   def __init__(self, value):
       self.next = None
       self.value = value
class Stack:
   def __init__(self):
       self.head = Node('head')
       self.size = 0
   def __str__(self): #__repr__
       cur = self.head.next
       out = ''
       while cur:
           out+=str(cur.value)+ '->'
           cur = cur.next
       return out[:-2]
   def getSize(self):
       return self.size
   def isEmpty(self):
       return not bool(self.size)
   def push(self, value):
       node = Node(value)
       node.next = self.head.next
       self.head.next = node
       self.size+=1
   def pop(self):
       if self.isEmpty():
           raise Exception('Popping from an empty stack')
       top = self.head.next
       self.head.next = top.next #self.head.next.next
       self.size -= 1
       return top.value
   def peek(self):
       if self.isEmpty():
           raise Exception('Stack is empty')
       return self.head.next.value
def copy(s1):
   # s1과 s2가 같은 객체가 되지 않도록 복사하는 함수
   s = Stack()
   arr = []
   while not s1.isEmpty():
       arr.append(s1.pop())
   arr.reverse()
   for i in arr:
       s.push(i)
       s1.push(i)
   return s
class Queue(object):
   def __init__(self):
       self.s1 = Stack()
       self.s2 = Stack()
   def enqueue(self, value):
       self.s1.push(value)
   def dequeue(self):
       if self.s1.isEmpty():
           raise Exception('Queue is empty')
       self.s2 = Stack()
       #s1의 맨 첫 원소를 제외한 원소를 s2에 역순으로 집어넣음
       for i in range(self.s1.getSize()-1):
           self.s2.push(self.s1.peek())
           self.s1.pop()
       #return값에 s1의 맨 앞 값을 집어넣음
       ret = self.s1.pop()
       #s2에 있는 역순 배열된 s1의 첫 원소를 제외한 원소들을 다시 원래 순서대로 s1에 집어넣음
       v = self.s2.getSize()
       for i in range(v):
           self.s1.push(self.s2.peek())
           self.s2.pop()
       return ret
   def size(self):
       return self.s1.getSize()
   def peek(self):
       if self.s1.isEmpty():
           raise Exception('Queue is empty')
       #기억 용도로 s2에 s1을 복제함
       self.s2 = copy(self.s1)
       #s1의 첫 원소를 제외한 원소를 모두 pop함
       for i in range(self.s1.getSize() - 1):
           self.s1.pop()
       #s1의 첫 원소를 return값에 저장함
       ret = self.s1.peek()
       #다시 s1에 s2를 복제함
       self.s1 = copy(self.s2)
       return ret
   def isEmpty(self):
       return self.s1.isEmpty()
q = Queue()
for i in range(5):
   q.enqueue(i)
print(q.size())
print(q.peek())
for i in range(5):
   print(q.dequeue())
q.dequeue()
