N = int(input())

for i in range (N) :
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    cnt = 0
    for j in arr[1:] :
        if  j > avg :
            cnt += 1
        rate = cnt / arr[0] * 100
    print(f'{rate:.3f}%')