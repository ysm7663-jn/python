N = int(input())

result = []

if N % 2 == 0:
    for i in range(N):
        if i % 2 == 0:
            result.append(1)
        else:
            result.append(2)
else:
    for i in range(N-1):
        if i % 2 == 0:
            result.append(1)
        else:
            result.append(2)
    result.append(3)

for i in result:
    print(i, end=' ')
print()
# *list이름 = iterator 안의 요소를 모두 출력해준다.
print(*result)