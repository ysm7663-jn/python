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
            if self.current_node.value == value : # 일치하면 True 반환
                return True
            elif value < self.current_node.value :  # 왼쪽에 있는지
                self.current_node = self.current_node.left
            else : # 오른쪽에 있는지
                self.current_node = self.current_node.right
        return False    # 순회를 통해서 일치하는 노드가 없으면 False 반환
    
    # 4-4 노드 삭제
    # 삭제를 위해 해당 노드가 있는지 확인
    def delete(self, value) :
        searched = False
        self.current_node = self.head # 루트 노드 / 삭제할 노드
        self.parent = self.head # 삭제할 노드의 부모 노드
        while self.current_node:
            if self.current_node.value == value : # 값을 찾으면 True 반환하고 while 문 종료
                searched = True
                break
            elif value < self.current_node.value :
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else :
                self.parent = self.current_node
                self.current_node = self.current_node.right
        # 해당 노드가 트리에 없는 경우
        if searched == False :
            return False

    # Case별 코드 작성
    # 4-4-1 Leaf Node 삭제
    # self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 형태
        if self.current_node.left == None and self.current_node.right == None : # 자식이 없는 상태
            if value < self.parent.value :
                self.parent.left = None
            else :
                self.parent.right = None

    # 4-4-2 Child Node가 한 개인 Node 삭제
        # 왼쪽에만 child_node가 있는 경우
        elif self.current_node.left != None and self.current_node.right == None :
            if value < self.parent.value :
                self.parent.left = self.current_node.left
            else :
                self.parent.right = self.current_node.left
        # 오른쪽에만 child_node가 있는 경우
        elif self.current_node.left == None and self.current_node.right != None :
            if value < self.parent.value :
                self.parent.left = self.current_node.right
            else :
                self.parent.right = self.current_node.right

    # 4-4-3 Child Node가 두 개인 Node 삭제
        elif self.current_node.left != None and self.current_node.right != None: # Child Node가 두 개인 경우
            if value < self.parent.value : # 삭제할 Node가 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 있을 때와 없을 때
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None : # 바뀌는 노드의 왼쪽 자식(더 작은 수)의 존재 확인
                    self.change_node_parent = self.change_node # 기존 chang_node는 부모로 변경
                    self.change_node = self.change_node.left # 더 작은 수를 chang_node로 변경
                # 대체되는 노드의 오른쪽 자식이 있을 경우
                if self.change_node.right != None :
                    self.change_node_parent.left = self.change_node.right
                else :
                    self.change_node_parent.left = None
                # 삭제된 노드로 옮겨간 chang_node에 대한 연결 정리
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else : # 삭제할 Node가 오른쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node의 있을 Child Node가 때와 없을 때
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None :
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None :
                    self.change_node_parent.left = self.change_node.right
                else :
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

# 1 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
# random 라이브러리 : random.randint(0, 999) : 0에서 999까지 숫자중 특정 숫자를 랜덤하게 선택해서 리턴해줌
import random

# 1 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_num = set() # 중복 제거를 위해 사용
while len(bst_num) != 100 :
    bst_num.add(random.randint(0, 999))

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함(중앙값)
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_num :
    binary_tree.insert(num)

for num in bst_num :
    if binary_tree.search(num) == False :
        print('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_num = set()
bst_num = list(bst_num)
while len(delete_num) != 10 :
    delete_num.add(bst_num[random.randint(0, 99)])

# 선택한 10기의 숫자를 삭제(삭제 기능 확인)
for del_num in delete_num :
    if binary_tree.delete(del_num) == False :
        print('delete failed', del_num)

"""
5. 이진 탐색 트리의 시간 복잡도와 단점
5-1. 시간 복잡도 (탐색시)
    - depth (트리의 높이)를 h라고 표기한다면, O(h)
    - n개의 노드를 가진다면, h = log2n에 가까우므로, 시간 복잡도는 O(logn)

5-2. 이진 탐색 트리
    - 평균 시간 복잡도 : O(log n)
    - 최악 시간 복잡도 : O(n)  >> 최악의 경우 = 링크드 리스트와 동일한 성능을 보여줌 (1(root node) - 2 - 3 - 4 - 5) 
"""