N = int(input())
data_list = set(map(int, input().split()))
M = int(input())
data_list2 = list(map(int, input().split()))

for i in data_list2:
    if i not in data_list:
        print('0')
    else:
        print('1')