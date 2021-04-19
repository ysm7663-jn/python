# 너비 우선 탐색 (Breadth-First Search, BFS)
"""
정점들과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식
>> 한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들(형제 노드들)을 먼저 순회함

파이썬으로 그래프를 표현하는 방법
>> 파이썬에서 제공하는 딕셔너리와 리스트 자려 구조를 활용해서 그래프를 표현할 수 있음
"""
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph) # {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'G', 'H', 'I'], 'D': ['B', 'E', 'F'], 'E': ['D'], 'F': ['D'], 'G': ['C'], 'H': ['C'], 'I': ['C', 'J'], 'J': ['I']}

def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    # visited : 큐 / need_visit : 큐
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited

print(bfs(graph,'A')) # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
"""
시간 복잡도 = O(V + E)
노드 수 : V / 간선 수 : E