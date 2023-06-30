from linkedlistFIFO import LinkedListFIFO
import random
class HashTableLL:
   def __init__(self, size):
       self.size = size
       self.count = 0
       self.slots=[]
       self._createHashTable()
   def _createHashTable(self):
       for i in range(self.size):
           self.slots.append(LinkedListFIFO())

   def _find(self, item):
       return item % self.size

   def _add(self, item):
       self.slots[self._find(item)].addNode(item)
       self.count+=1

   def _delete(self, item):
       self.slots[self._find(item)].deleteNodeByValue(item)
       self.count-=1

   def _print(self):
       for i in range(self.size):
           print(f"슬롯(slot) {i}:")
           self.slots[i]._printlist()
   def loadFactor(self):
       return self.count/self.size
class HashOpenAddressing:
   def __init__(self, size):
       self.size = size
       self.count = 0
       self.slots = []
       self._createHashTable()

   def _createHashTable(self):
       for i in range(self.size):
           self.slots.append(LinkedListFIFO())

   def _find(self, item):
       return item % self.size

   def _add(self, item, location = None):
       if location == None:
           location = item
       if self.slots[self._find(location)].length==0:
           self.slots[self._find(location)].addNode(item)
           self.count += 1
       else:
           print(f"{item}과 {self.slots[self._find(location)].head.value}가 충돌")
           self._add(item, location+1)

   def _delete(self, item, location = None):
       if location == None:
           location = item
       a, b, found = self.slots[self._find(location)]._find_by_value(item)
       if found:
           self.slots[self._find(location)].deleteNodeByValue(item)
           self.count-=1
       else:
           self._delete(item, location+1)

   def _print(self):
       for i in range(self.size):
           print(f"슬롯(slot) {i}:")
           self.slots[i]._printlist()
   def loadFactor(self):
       return self.count/self.size

def test_hash_tables():
   H1 = HashTableLL(3)
   for i in range(0, 20):
       H1._add(i)
   H1._print()
   print("\n항목 0,1,2를 삭제합니다.")
   H1._delete(0)
   H1._delete(1)
   H1._delete(2)
   H1._print()
   print(f'해시 테이블의 Load Factor : {H1.loadFactor()}')
   print()
def test_hash_tables_with_OpenAdressing():
   H =  HashOpenAddressing(35)
   list = []
   for i in range(34):
       v = random.randint(0,10000)
       H._add(v)
       list.append(v)
   print('초기 해시 테이블 출력')
   H._print()
   print(f'해시 테이블의 Load Factor : {H.loadFactor()}')
   for i in range(len(list)):
       if i%10==0 and i:
           print()
           print(f'{i}개의 원소를 삭제한 해시 테이블 출력')
           H._print()
           print(f'해시 테이블의 Load Factor : {H.loadFactor()}')
       H._delete(list[i])

if __name__ == '__main__':
   test_hash_tables()
   test_hash_tables_with_OpenAdressing()


