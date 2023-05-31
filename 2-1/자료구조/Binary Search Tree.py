class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    # 아래 함수들은 연산 이후 원래 n이 있던 위치에 있어야 할 노드를 리턴.
    def preorder(self, node):
        if node == None:
            return
        print(node.key, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.key, end=' ')
        self.inorder(node.right)
    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key, end=' ')
    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, k):
        if n == None:
            return None
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)
        # self.root == None 이면 새 노드 생성, 아니면 그대로.

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root == None:
            print('Tree is empty')
        self.root = self.del_min(self.root)
        # root가 min인 경우에 root를 교체해 줌.

    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n
    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)
        elif n.key < k:
            n.right = self.del_node(n.left, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n

if __name__ == '__main__':
    t = BST()
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t',end='')
    t.inorder(t.root)
    print('\n250: ',t.get(250))
    t.delete(200)
    print('200 삭제 후:')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t',end='')
    t.inorder(t.root)