import sys

N = int(sys.stdin.readline())

for i in range(N):
    stack = list(sys.stdin.readline())

    sum = 0

    for j in range(len(stack)):
        if stack[j] == '(':
            sum += 1
        elif stack[j] == ')':
            sum -= 1
        
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')