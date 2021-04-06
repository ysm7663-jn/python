""" 
트리 : Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
: 이진트리 형태의 구조 >> 탐색 알고리즘 구현을 위해 많이 사용됨

1) 용어
Node : 트리에서 데이터를 저장하는 기본 요소(데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
Root Node : 트리 맨 위에 있는 노드
Level : 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
Parent Node : 어떤 노드의 다음 레벨에 연결된 노드
Child Node : 어떤 노드의 상위 레벨에 연결된 노드
Leaf Node (Terminal Node) : Child Node가 하나도 없는 노드
Siblings (Brother Node) : 동일한 Parent Node를 가진 노드
Depth : 트리에서 Node를 가질 수 있는 최대 Level

2) 이진 트리 와 이진 탐색 트리(Binary Search Tree)
- 이진 트리 : 노드의 최대 Branch가 2인 트리
- 이진 탐색 트리 : 이진 트리에다음과 같은 추가적인 조건이 있는 트리
    : 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보 다 큰 값을 가지고 있음

3) 자료 구조 이진 탐색 트리의 장점과 주요 용도
- 주요 용도 : 데이터 검색(탐색)
- 장점 : 탐색 속도를 개선할 수 있음

4) 노드 클래스 만들기
"""
# 4-1 노드 클래스 / 루트 노드 설정
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt :
    def __init__(self, head) :
        self.head = head # 루트 노드

    # 4-2 노드 삽입
    def insert(self, value) :
        self.current_node = self.head
        while True :
            if value < self.current_node.value: # 왼쪽 노드 탐색
                if self.current_node.left != None:  # 왼쪽 노드에 값이 존재하면
                    self.current_node = self.current_node.left # 탐색의 값을 변경
                else : 
                    self.current_node.left = Node(value) # value와 같은 노드가 없으면 추가
                    break
            else : # 오른쪽 노드 탐색
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else :
                    self.current_node.right = Node(value)
                    break

    # 4-3 노드 탐색
    def search(self, value) :
        self.current_node = self.head # 루트 노드부터 시작
        while self.current_node : # 노드가 존재할때 까지
            if self.current_node.value == value :
                return True
            elif value < self.current_node.value :
                self.current_node = self.current_node.left
            else :
                self.current_node = self.current_node.right
        return False

    # 4-4 노드 삭제
    # 4-4-1 Leaf Node 삭제
    # 4-4-2 Child Node가 한 개인 Node 삭제
    # 4-4-3 Child Node가 두 개인 Node 삭제
    """
    1. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다
        - 삭제할 Node의 오른쪽 자식 선택
        - 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
        - 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
        - 해당 Node의 왼쪽 Branch가 삭제할 왼쪽 Child Node를 가리키게 함
        - 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
        - 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는, 해당 Node의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함
    2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다. 
    """

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))
print(BST.search(-1))
print(BST.search(2))

