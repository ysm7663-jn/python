data_list = list(map(int, input().split(' ')))
"""
내 풀이
a = sorted(data_list)
b = sorted(data_list, reverse=True)

data_sort = []

for i in data_list:
    data_sort.append(i)

if a == data_sort:
    print('ascending')
elif b == data_sort:
    print('descending')
else:
    print('mixed')
"""

ascending = True
descending = True

for i in range(1, 8):
    if data_list[i] > data_list[i-1]:
        descending = False
    elif data_list[i] < data_list[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
