N = int(input())

data_list = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    data_list.append((age, name))

data_list.sort(key = lambda x : (x[0]))

for i in data_list:
    print(i[0], i[1])

"""
n = int(input())

array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array = sorted(array, key = lambda x: x[0])
for i in range array:
    print(i[0], i[1])
"""