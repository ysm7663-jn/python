import sys

N = int(sys.stdin.readline())

data = [25, 10, 5, 1]
count = [0 for i in range(4)]

for i in range(N):
    money = int(sys.stdin.readline())
    for j in range(len(data)):
        count[j] += money // data[j]
        money %= data[j]
        print(count[j], end=' ')
    count = [0 for i in range(4)]
    print()