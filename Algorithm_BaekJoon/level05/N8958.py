N = int(input())

for i in range (N) :
    arr = list(input())
    sum = 0
    cnt = 1
    for j in arr :
        if j == 'O' :
            sum += cnt
            cnt += 1
        else :
            cnt = 1
    print(sum)