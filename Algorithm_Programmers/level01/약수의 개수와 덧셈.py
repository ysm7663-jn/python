# 약수 구하는 방법 : i(대상) % j(증감) == 0이면 j는 i의 약수
def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer 

print(solution(13, 17))
print(solution(24, 27))
"""
# 정답은 맞음 > 타임 오버
for i in range(left, right+1):
    count = 0
    for j in range(2, i):
        n = j 
        while n < i:
            if j * n == i:
                print('j * n', j, n)
                if j == n:
                    count += 1
                else:
                    count += 2
                print('count',count)
                break
            else:
                n += 1

    if count % 2 == 0:
        answer += i
        print('if answer', answer)
    else:
        answer -= i
        print('else answer', answer)

return answer
"""