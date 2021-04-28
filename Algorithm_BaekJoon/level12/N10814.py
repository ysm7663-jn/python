N = int(input())

data_list = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    data_list.append((age, name))

print(data_list)
data_list.sort(key = lambda x : (x[0]))

for i in data_list:
    print(i[0], i[1])
