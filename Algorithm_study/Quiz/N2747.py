import sys

n = int(sys.stdin.readline())

sum = [0 for i in range(n+1)]

sum[1] = 1

for i in range(2, len(sum)):
    sum[i] = sum[i-1] + sum[i-2]

print(sum[-1])