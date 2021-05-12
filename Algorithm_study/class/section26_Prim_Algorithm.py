# 프림 알고리즘 (Prim Algorithm)
"""
순서
    1) 임의의 정점을 선택, '연결된 노드 집합'에 삽입
    2) 선택된 정점에 연결된 간선들을 간선 리스트에 삽입
    3) 간선 리스트에서 최소 가중치를 가지는 간선부터 추출해서,
        - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면, 스킵함(cycle 발생을 막기 위함)
        - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않으면, 해당 간선을 선택하고, 해당 간선 정보를 '최소 신장 트리'에 삽입
    4) 추출한 간선은 간선 리스트에서 제거
    5) 간선 리스트에 더 이상의 간선이 없을 때까지 3-4번 반복
"""
# heapq.heappush를 통해 데이터를 heap 형태로 넣을 수 있음(0번 인덱스를 우선순위로 인지함)
import heapq

queue = []
graph_data = [[2,'A'], [5,'B'], [3,'C']]

for edge in graph_data:
    heapq.heappush(queue, edge)

for index in range(len(queue)):
    print(heapq.heappop(queue))

print(queue)

# heapq.heapify() 함수를 통해 리스트 데이터를 heap 형태로 한 번에 변환할 수 있음(0번 인덱스를 우선순위로 인지함)
import heapq

queue = []
graph_data = [[2,'A'], [5,'B'], [3,'C']]

heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

print(graph_data)

# collections 라이브러리의 defaultdict 함수 활용하기
#   - defaultdict 함수를 사용해서, key에 대한 value를 지정하지 않았을 시, 빈 리스트로 초기화하기
from collections import defaultdict

list_dict = defaultdict(list)
# list_dict = defaultdict(int) > 0
print(list_dict['key1'])

""" 
오류 발생
key에 대한 초기화가 안 되어있기 때문에
list_dict2 = dict()
print(list_dict['key2'])
"""

"""
프림 알고리즘
0. 모든 간선 정보를 저장 (adjacent_edges)
1. 임의의 정점을 선택, '연결된 노드 집합(connected_nodes)'에 삽입
2. 선택된 정점에 연결된 간선들을 간선 리스트(candidate_edge_list)에 삽입
3. 간선 리스트(candidate_edge_list)에서 최소 가중치를 가지는 간선부터 추출해서,
    - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면, 스킵함(cycle 발생을 막기 위함)
    - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않으면, 해당 간선을 선택하고, 해당 간선 정보를 '최소 신장 트리(mst)'에 삽입
        - 해당 간선에 연결된 인접 정점의 간선들 중, '연결된 노드 집합(connected_codes)'에 없는 노드와 연결된 간선들만 간선 리스트(candidate_edge_list)에 삽입
            - '연결된 노드 집합 (connected_nodes)'에 있는 노드와 연결된 간선들을 간선 리스트에 삽입해도, 해당 간선은 스킵될 것이기 때문임
            - 어차피 스킵될 간선을 간선 리스트(candidate_edge_list)에 넣지 않으므로 해서, 간선 리스트(candidate_edge_list)에 최소 가중치를 가지는 간선부터 추출하기 위한 자료구조 유지를 위한 effort를 줄일 수 있음(최소힙 구조 사용)
4. 선택된 간선은 간선 리스트에서 제거
5. 간선 리스트에 더 이상의 간선이 없을 때까지 3-4번을 반복
"""

edges = [
    (7,'A','B'), (5,'A','D'),
    (8,'B','C'), (9,'B','D'),(7,'B','E'),
    (5,'C','E'), 
    (7,'D','E'), (6,'D','F'),
    (8,'E','F'), (9,'E','G'),
    (11,'F','G')
]

from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

        # 인접 정접의 간선 리스트
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst

print(prim('A', edges))
# [(5, 'A', 'D'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (5, 'E', 'C'), (9, 'E', 'G')]

"""
시간복잡도 : O(E log E)
