N, M, S = map(int, input().split())

matrix = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0] * (N+1)

def dfs(S) :
    visit_list[S] = 1
    print(S, end=' ')
    
    for i in range(1, N+1):
        if visit_list[i] == 0 and matrix[S][i] == 1:
            print(visit_list)
            dfs(i)

dfs(S)