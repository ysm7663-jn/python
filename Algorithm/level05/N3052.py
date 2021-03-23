import sys

arr = []

for i in range(10) :
    n = int(sys.stdin.readline())
    arr.append(n % 42)
# [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
# set을 활용하여 중복 제거
arr = set(arr)
# {0, 1, 2, 39, 40, 41}
print(len(arr))

