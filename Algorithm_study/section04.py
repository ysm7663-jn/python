"""
4. 링크드 리스트(Linked List)
    1) 링크드 리스트 구조
        - 연결 리스트
        - 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
        - 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

        링크드 리스트 기본 구조와 용어
        노드(Node) : 데이터 저장 단위(데이터값, 포인터) 로 구성
        포인터(Pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

    2) 간단한 링크드 리스트 예

"""
class Node :
    def __init__(self, data, next=None) : # next는 None으로 디폴트
        self.data = data
        self.next = None

node1 = Node(1) 
node2 = Node(2)
node1.next = node2
head = node1

print('-----')

""" 
링크드 리스트로 데이터 추가
"""
class Node :
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

    def add(data) :
        node = head
        while node.next :
            node = node.next
        node.next = Node(data)

    for i in range(1, 10) : # 1 ~ 9까지를 linked list에 추가
        add(i)

    node = head
    while node.next :
        print(node.data) # 1 2 1 2 3 4 5 6 7 8
        node = node.next
    print(node.data) # 9

    print('-----')

""" 
장점 : 미리 데이터 공간을 미리 할당하지 않아도 됨
단점 : 
    - 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
    - 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
    - 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요


기존 노드 사이에 데이터 추가
"""
node3 = Node(1.5)

node = head
search = True
while search :
    if node.data == 1:
        search = False
    else :
        node = node.next

    node_next = node.next
    node.next = node3
    node3.next = node_next

node = head
while node.next :
    print(node.data)
    node = node.next
print(node.data)

print('-----')

""" 
5. 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현
"""
class Node :
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

class NodeMgmt :
    def __init__(self, data) :
        self.head = Node(data)

    def add(self, data) :
        if self.head == "":
            self.head = Node(data)
        else :
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    def desc(self) :
        node = self.head
        while node :
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)

for data in range(1, 10) :
    linkedlist1.add(data)
linkedlist1.desc()

"""
6. 링크드 리스트 특정 노드 삭제
"""
class Node :
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

class NodeMgmt :
    def __init__(self, data) :
        self.head = Node(data)

    def add(self, data) :
        if self.head == "":
            self.head = Node(data)
        else :
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self) :
        node = self.head
        while node :
            print(node.data)
            node = node.next
    
    def delete(self,data) :
        if self.head == "" :
            print("해당 값을 가진 노드가 없습니다.")
            return
        # 1) head 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp

        # 2) 마지막, 중간 노드 삭제
        else :
            node = self.head
            while node.next :
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else :
                    node = node.next


linkedlist1 = NodeMgmt(0)

for data in range(1, 10) :
    linkedlist1.add(data)
linkedlist1.desc()

print('-------')

linkedlist1 = NodeMgmt(100)
linkedlist1.desc()

print('-------')

# head를 지움
linkedlist1.delete(0)
linkedlist1.head

for data in range(1, 10) :
    linkedlist1.add(data)
linkedlist1.desc()

print('----------')

linkedlist1.delete(4)
linkedlist1.desc()

print('!!!!!!!!!!!!')


"""
7. 다양한 링크드 리스트 구조
    - 더블 링크드 리스트 기본구조
        : 이중 연결 리스트라고 함
    - 장점 : 양방향으로 연결되어 있어서노드 탐색이 양쪽 모두 가능
"""
class Node :
    def __init__(self, data, next=None, prev=Node) :
        self.data = data
        self.prev = prev
        self.next = next

class Nodemgmt:
    def __init__(self, data) :
        self.head = Node(data)
        self.tail = self.head
    
    def insert(self, data) :
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head
        else :
            node = self.head
            while node.next :   # 노드의 끝을 찾는 작업
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
    
    def desc(self) :
        node = self.head
        while node :
            print(node.data)
            node = node.next

    def search_from_head(self, data) :
        if self.head == None :
            return False

        node = self.head
        while node:
            if node.data == data :
                return node
            else :
                node = node.next
        return False # 찾는 값이 없다.

    def search_from_tail(self, data) :
        if self.head == None :
            return False

        node = self.tail
        while node:
            if node.data == data :
                return node
            else :
                node = node.prev
        return False # 찾는 값이 없다.

    def insert_before(self, data, before_data) :
        if self.head == None :
            slef.head = Node(data)
            return True
        
        else :
            node = self.tail
            while node.data != before_data :
                node = node.prev
                if node == None :
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

    def insert_after(self, data, after_data) :
        if self.head == None:
            self.head = Node(data)
            return True            
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True


double_linked_list = Nodemgmt(0)

for data in range(1, 10) :
    double_linked_list.insert(data)
double_linked_list.desc()

print('@@@@')

node_3 = double_linked_list.search_from_head(10)
if node_3 : 
    print(node_3.data)
else :
    print('No data')

print('@@@@')

node_3 = double_linked_list.search_from_tail(8)
if node_3 : 
    print(node_3.data)
else :
    print('No data')

print('#####')

# 연습 문제1. 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수 만들기
double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()
print('$$$$$$')
double_linked_list.insert_after(3.5, 3)
double_linked_list.desc()