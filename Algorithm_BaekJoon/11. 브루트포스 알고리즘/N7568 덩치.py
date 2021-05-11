import sys

N = int(sys.stdin.readline())

data_list = []

for i in range(N):
    data_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j: continue
        if data_list[i][0] < data_list[j][0] and data_list[i][1] < data_list[j][1]:
            rank += 1        
    print(rank, end=' ')  