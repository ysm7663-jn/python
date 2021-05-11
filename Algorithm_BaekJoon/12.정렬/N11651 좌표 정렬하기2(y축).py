import sys

N = int(sys.stdin.readline())

data_list = []

for _ in range(N):
    data_list.append(list(map(int, sys.stdin.readline().split())))
# x[1](y축) 정렬 > x[0](x축) 정렬
data_list.sort(key=lambda x : (x[1], x[0]))

for i in data_list:
    print(i[0], i[1])