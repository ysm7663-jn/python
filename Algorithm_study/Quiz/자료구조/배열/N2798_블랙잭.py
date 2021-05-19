N, M = map(int, input().split())

data_list = list(map(int, input().split()))

max = 0
for i in range(len(data_list)):
    for j in range(i+1, len(data_list)):
        for k in range(j+1, len(data_list)):
            sum = data_list[i] + data_list[j] + data_list[k]
            if  sum > max and sum <= M:
                max = sum
print(max)
        
