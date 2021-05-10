import sys

while True:
    try :
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

    except:
        break

# 파이썬에서의 try - catch문