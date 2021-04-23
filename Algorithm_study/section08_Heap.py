"""
힙 (Heap) 이란?
: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리
    - 완전 이진 트리 : 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

1. 힙을 사용하는 이유
: 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림
: 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면 O(logn)이 걸림
: 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

2. 힙의 구조
1) 최대 힙 (Max Heap) : 최대값을 구하기 위한 구조
2) 최소 힙 (Min Heap) : 최소값을 구하기 위한 구조
    - 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다 (최대 힙의 경우)
    - 긱 노드의 값은 해당 노드의 자식 노드가 가진 값보다 작거나 같다 (최소 힙의 경우)
3) 완전 이진 트리의 형태를 가짐


4) 힙과 이진 탐색 트리의 공통점과 차이점
공통점 : 힙과 이진 탐색 트리는 모두 이진 트리
차이점 :
    - 힙은 각 노드의 값이 자식 노드보다 크거나 같음
    - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼 (힙은 이 조건이 없음(왼쪽 자식이 더 클수도, 작을수도 있음))
    - 이진 탐색 트리 - 탐색 / 힙 - 최대or최소 값 검색

3. 힙 동작
1) 힙에 데이터 삽입하기 - 기본 동작
: 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워디는 형태로 삽입

1-1) 힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap 의 예)
: 먼저 삽입된 데이터는 완전 이진 트리에 맞추어, 최하단 왼쪽 노드부터 채워짐
: 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함 (swap)

2) 힙의 데이터 삭제하기 (Max Heap 의 예)
: 보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
    - 힙의 용도는 최대값과 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것
: 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드 (일반적으로 가장 마지막에 추가한 노드)를 root 노드로 이동
: root 노드의 값이 child node 보다 작을 경우, root노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)

4. 힙 구현
힙과 배열
: 일반적으로 힙 구현시 배열 자료구조를 활용
: 배열은 인덱스가 0부터 시작하지만, 힙 구현의 편의를 위해 root 노드 인덱스 번호를 1로 지정하면, 구현이 좀 더 수월함
    - 부모 노드 인덱스 번호 (parent's index) = 자식 노드 인덱스 번호 (child node's index) // 2
    - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2
    - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2 + 1
"""
class Heap :
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # index 0번자리에 None을 배치함으로써 계산을 손쉽게 할 수 있게 함
        self.heap_array.append(data)

# heap = Heap(1)
# print(heap.heap_array) # [None, 1]

    # 상위 노드와의 swap 
    def move_up(self, inserted_idx) :
        if inserted_idx <= 1: # root node 일 때
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx] : # 입력 받은 값이 부모 값 보다 더 큰 경우 
            return True # True를 반환하여 아래 while문에서 swap이 이뤄지도록 함
        else :
            return False # 부모 값이 더 크거나, root node 일 때 


    # 데이터 삽입 (맨 마지막에 들어감)
    def insert(self, data):
        if len(self.heap_array) == 0: # 루트 노드가 없을 경우
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        # 데이터가 이미 들어가 있는 경우
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx) :
            parent_idx = inserted_idx // 2 # 부모 노드
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swap / 부모 노드와 입력 받은 노드와 swqp
            inserted_idx = parent_idx # 바뀌었기 때문에, 바뀐 후 부모와 비교
        return True
    
    def move_down(self, popped_idx) :
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1 : 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        
        # case2 : 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        
        # case3 : 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    # 데이터 삭제
    def pop(self) :
        if len(self.heap_array) <= 1:
            return None
         
        # root node 추출   
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1] # 맨 끝 node를 root node로 옮김
        del self.heap_array[-1] # 맨 끝 node 삭제
        popped_idx = 1

        while self.move_down(popped_idx) :
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1 

            # case2 : 오른쪽 자식 노드만 없을 때, 왼쪽 자식은 존재
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx] :
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                
            # case3 : 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx] :
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                    
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx
        return returned_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
heap.pop()
print(heap.heap_array)

"""
5. 힙 시간 복잡도
: depth(트리의 높이)를 h라고 표기한다면,
: n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h = logn에 가까우므로, 시간 복잡도는 O(logn)
    - 한번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미. 즉 50%ㅇ의 실행시간을 단축시킬 수 있다는 것을 의미함