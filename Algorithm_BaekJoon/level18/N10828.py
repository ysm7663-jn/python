import sys

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def top():
    if len(stack) == 0:
        return -1
    else:
        return int(stack[-1])

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

N = int(sys.stdin.readline().rstrip())

stack = list()

for i in range(N):
    read_line = sys.stdin.readline().rstrip().split()

    order = read_line[0]

    if order == 'push':
        push(read_line[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'top':
        print(top())
    elif order == 'empty':
        print(empty())