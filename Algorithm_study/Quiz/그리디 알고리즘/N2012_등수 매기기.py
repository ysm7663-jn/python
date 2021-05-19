import sys

N = int(sys.stdin.readline())
"""
# 시간 초과
expect_rank = [0] * N
real_rank = [0] * N

for i in range(N):
    expect_rank[i] = [i, int(input())]
    real_rank[i] = [i, i+1]
expect_rank = sorted(expect_rank, key = lambda x : x[1])

sum = 0
for i in range(len(real_rank)):
    if real_rank[i][1] != expect_rank[i][1]:
        sum += abs(real_rank[i][1] - expect_rank[i][1])

print(sum)
"""
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()

sum = 0

for i in range(1, len(data) +1 ):
    sum += abs(i - data[i-1])

print(sum)