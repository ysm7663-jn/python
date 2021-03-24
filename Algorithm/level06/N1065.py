N = int(input())

cnt = 0

for i in range(1, N+1) :
    if i < 100 :
        cnt += 1
        
    else :
        arr = list(map(int, str(i))) 
        if arr[0] - arr[1] == arr[1] - arr[2] :
            cnt += 1
    
print(cnt)    