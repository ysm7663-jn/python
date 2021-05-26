N = int(input())

data_list = list(map(int, input().split()))

data_list.sort()

result = []
num = 0

for i in data_list:
    num += i
    result.append(num)
print(sum(result))