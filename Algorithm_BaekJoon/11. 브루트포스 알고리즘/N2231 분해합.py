import sys

N = int(sys.stdin.readline())

result = 0

for i in range(N):
    num = i
    sum = 0
    while num != 0:
        sum += (num % 10)
        num //= 10
    
    if i + sum == N:
        result = i
        break
print(result)