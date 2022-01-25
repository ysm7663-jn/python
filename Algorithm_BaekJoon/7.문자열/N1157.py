arr = input().upper()

unique_arr = list(set(arr))

count_arr = []
for i in unique_arr :
    cnt = arr.count(i)
    count_arr.append(cnt)

print(count_arr)

if count_arr.count(max(count_arr)) > 1 :
    print('?')
else :
    max_index = count_arr.index(max(count_arr))
    print(unique_arr[max_index])

    