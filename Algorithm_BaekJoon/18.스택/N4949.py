while True:
    line = input()

    if line == '.':
        break

    stack = []
    stat = True
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if len(stack) == 0:
                stat = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                stat = False
                break

        elif i == ']':
            if len(stack) == 0:
                stat = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                stat = False
                break
    if stat and not stack:
        print('yes')
    else:
        print('no')