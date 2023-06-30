class Node:
   def __init__(self, data=None):
       self.data = data
       self.prev = None
       self.next = None

class DoublyLinkedList:
   def __init__(self):
       self.head = None
       self.tail = None

   def add_node(self, data):
       new_node = Node(data)

       if self.head is None:
           self.head = new_node
           self.tail = new_node
       else:
           cur = self.tail
           cur.next = new_node
           new_node.prev = cur
           self.tail = new_node

   def remove_node(self, data):
       if self.head is None:
           return

       cur = self.head
       while cur:
           if cur.data == data:
               if cur == self.head and cur == self.tail:
                   self.head = None
                   self.tail = None
               elif cur == self.head:
                   self.head = cur.next
                   cur.next.prev = None
               elif cur == self.tail:
                   self.tail = cur.prev
                   cur.prev.next = None
               else:
                   cur.prev.next = cur.next
                   cur.next.prev = cur.prev
               return
           cur = cur.next

   def traverse_left_to_right(self):
       cur = self.head
       while cur:
           print(cur.data, end= ' ')
           cur = cur.next
       print()

   def traverse_right_to_left(self):
       cur = self.tail
       while cur:
           print(cur.data, end = ' ')
           cur = cur.prev
       print()

if __name__ == '__main__':
   dll = DoublyLinkedList()
   for i in range(1, 10):
       dll.add_node(i)
   dll.remove_node(4)
   dll.remove_node(8)
   dll.add_node(5)
   dll.traverse_left_to_right()
   dll.traverse_right_to_left()


