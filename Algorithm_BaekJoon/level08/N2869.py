import math
A, B, V = map(int, input().split())

day = math.ceil((V-A)/(A-B)) + 1
print(day)

"""
while True:
    count += 1
    if A * count - B * (count - 1) >= V:
        break
print(count)
시간 초과
"""
"""
data = list()
while True:
    for i in range(A):
        data.append(i)

    for j in range(B):
        del data[-1]

    if len(data) == V:
        print(count)
        break
    count += 1
시간 초과
"""