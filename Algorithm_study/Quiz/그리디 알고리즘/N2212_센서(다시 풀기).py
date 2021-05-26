N = int(input())
K = int(input())

if K >= N:
    print(0)
    exit()

data_list = sorted(list(map(int, input().split())))

distance = []

for i in range(1, len(data_list)):
    distance.append(data_list[i] - data_list[i-1])

distance.sort(reverse=True)

for i in range(K-1):
    distance.pop(0)

print(sum(distance))