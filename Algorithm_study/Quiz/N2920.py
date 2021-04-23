data_list = list(map(int, input().split()))

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