import sys

N = int(sys.stdin.readline())

data_list = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    data_list.append((x, y))
data_list.sort()
for i in range(len(data_list)):
    print(data_list[i][0], data_list[i][1])