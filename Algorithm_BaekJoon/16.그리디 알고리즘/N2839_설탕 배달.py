N = int(input())

count = []
five = N // 5
three = N // 3

for i in range (five+1):
    for j in range(three+1):
        if 5 * i + 3 * j == N:
            count.append(i + j)

if len(count) == 0:
    print(-1)
else:
    print(min(count))
