'''
#Stack with Linked list
class Node(object):
   def __init__(self, value = None, pointer = None):
       self.value = value
       self.pointer = pointer

class Stack(object):
   def __init__(self):
       self.head = None
       self.count = 0
   def isEmpty(self):
       return not bool(self.head)
   def push(self, item):
       self.head = Node(item, self.head)
       self.count += 1
   def pop(self):
       if self.count > 0 and self.head:
           node = self.head
           self.head = node.pointer
           self.count -= 1
           return node.value
       else:
           print('Stack is empty')
   def _printList(self):
       node = self.head
       while node:
           print(node.value, end=' ')
           node = node.pointer
       print()
   def peek(self):
       if self.count>0 and self.head:
           return self.head.value
       else:
           print('Stack is empty')
   def size(self):
       return self.count

s = Stack()
for i in range(10):
   s.push(i)
s._printList()
for i in range(5):
   s.pop()
s._printList()
print(s.peek())
'''
#두 번째 스택 코드
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
s = Stack()
for i in range(10):
   s.push(i)
print(s)
for i in range(5):
   print(f'Pop : {s.pop()}')
print(s, s.getSize())
print(s.peek())
for i in range(5):
   print(f'Pop : {s.pop()}')
print(s.isEmpty())
#s.peek() : Exception: Stack is empty
#s.pop() : Exception: Popping from an empty stack
# deque -> q.extendleft([5,3,1]) 식으로 하면 [1,3,5...]가 됨.
# deque -> q.remove(-3)같은 경우 값이 없으면 ValueError.
# deque -> q.rotate(1) : [1,2,3,4] -> [4,1,2,3] ->... -1로 하면 반대.
