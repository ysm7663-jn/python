# 깊이 우선 탐색 (Depth-First Search, DFS)

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

# need_visit : 스택 / visited : 큐
def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop() # pop() : list 맨 끝의 데이터 출력 / pop(0) : list 맨 앞의 데이터 출력 후 삭제

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

print(dfs(graph, 'A'))
"""
시간복잡도 : O(V + E)
노드 수 : V / 간선 수 : E