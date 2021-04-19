N = int(input())

num = N
cnt = 0

while True:
    ship = N // 10
    ill = N % 10

    sum = ship + ill
    N = ill * 10 + sum % 10 
    
    cnt += 1
    
    if N == num :
        print(cnt)
        break
    
    