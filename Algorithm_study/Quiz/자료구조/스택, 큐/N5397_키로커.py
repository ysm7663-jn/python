N = int(input())

for i in range(N):

    left_stack = []
    right_stack = []
    data = input()

    for j in data:
        if j == '-':
            if left_stack:
                left_stack.pop()
        elif j == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif j == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(j)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))