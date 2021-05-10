N = int(input())

count = 1
stack = []
result = []

for i in range(N):

    num = int(input())

    while count <= num:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))