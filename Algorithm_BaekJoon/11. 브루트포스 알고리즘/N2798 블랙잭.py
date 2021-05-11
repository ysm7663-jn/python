import sys

N, M = map(int, sys.stdin.readline().split())

data_list = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(len(data_list)):
    for j in range(i+1, len(data_list)):
        for k in range(j+1, len(data_list)):
            if data_list[i] + data_list[j] + data_list[k] > M:
                continue
            else:
                result.append(data_list[i] + data_list[j] + data_list[k])

print(max(result))