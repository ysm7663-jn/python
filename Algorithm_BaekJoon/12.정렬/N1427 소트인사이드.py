import sys

N = int(sys.stdin.readline())

data_list = list(str(N))
result = []
for i in range(len(data_list)):
    result.append(int(data_list[i]))
result = sorted(result, reverse=True)
for i in result:
    print(i, end='')

"""
array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')
"""