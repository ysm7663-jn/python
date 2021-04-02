"""
# 2번 

class Stack:
    def __init__(self):
        self.list = list()
 
    def push(self, data):
        self.list.append(data)
        
 
    def pop(self):
        return self.list.pop()
 
class Calculator:
    def __init__(self):
        self.stack = Stack()
 
    def calculate(self, string):

        for i in string :
            if i == ' ' :
                pass
            elif i == '+' :
                val2 = self.stack.pop()
                val1 = self.stack.pop()
                self.stack.push(val1 + val2)
            elif i == '-' :
                val2 = self.stack.pop()
                val1 = self.stack.pop()
                self.stack.push(val1 - val2)
            elif i == '*' :
                val2 = self.stack.pop()
                val1 = self.stack.pop()
                self.stack.push(val1 * val2)
            elif i == '/' :
                val2 = self.stack.pop()
                val1 = self.stack.pop()
                self.stack.push(int(val1 / val2))
            else :
                self.stack.push(int(i))
        return self.stack.pop()
 
# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))
"""
# 1번
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        if self.front == self.rear :
            return True
        else :
            return False
 
    def put(self, data):
        new_node = Node(data)
        self.rear.link = new_node
        self.rear = new_node
 
    def get(self):
        if not self.is_empty() :
            node = self.front
            value = node.data
            self.front = self.front.link
            del node
            return value
 
    def peek(self):
        return self.front.data
 
# Test code
queue = LinkedQueue()
 
print(queue.is_empty())
for i in range(10):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(11):
    print(queue.get(), end=' ')
print()
 
for i in range(20):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(5):
    print(queue.peek(), end=' ')
print()
 
for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())



class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class NodeMgmt :
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == "" :
            self.head = Node(data)
        else :
            node = self.head
            while node.next : # 다음 node가 있는 경우
                node = node.next
            node.next = Node(data)
    
    def desc(self) :
        node = self.head
        while node : # 노드가 존재할 경우
            print(node.data)
            node = node.next

    def delete(self, data) :
        if self.head == "" :
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        # 1) head 노드 삭제
        if self.head.data == data :
            temp = self.head
            self.head = self.head.next
            del temp

        # 2) 중간, 끝 노드 삭제
        else :
            node = self.head
            while node.next :
                if node.next.data == data : # 입력 받은 값이 다음 노드의 값일 경우
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else : # 다음 노드가 입력 값이 아닌 경우 그 다음 노드로 넘어간다.
                    node = node.next

linkedlist2 = NodeMgmt(0)

for data in range(1, 10) :
    linkedlist2.add(data)
linkedlist2.desc()