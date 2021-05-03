import sys

n = int(sys.stdin.readline())

sum = [0 for i in range(n+1)]

sum[1] = 1

for i in range(2, len(sum)):
    sum[i] = sum[i-1] + sum[i-2]

print(sum[-1])

"""
a, b = 0, 1
while n > 0:
    a, b = b, a + b
    n -= 1
print(a)
"""