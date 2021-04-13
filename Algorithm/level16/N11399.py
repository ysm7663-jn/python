n = int(input())
data = list(map(int,input().split()))
data.sort()

sum_data = 0
result = []

for i in range(len(data)) :
    sum_data += data[i]
    result.append(sum_data)
print(sum(result))