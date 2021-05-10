A, B, C = map(int,input().split())
"""
기존 코딩 문제점
: 예외(손익분기점이 나오지 않음) 상황을 짤 수 없음
bep = 0

n = 0

while True :

    if C * n > A + B * n:
        bep = n
        break
    n += 1 
print(bep)
"""
if B >= C :
    print(-1)
else :
    print(A // (C - B) + 1)
