import sys
# O(nlogn)
N = int(sys.stdin.readline())

data_list = []

for i in range(N):
    data_list.append(int(sys.stdin.readline()))

data_list.sort()

for i in data_list:
    print(i)

"""
# 선택정렬
# O(n^2)
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)
"""