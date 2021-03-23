N = int(input())

for i in range(0, N) :
    for j in range(0, i+1) :
        for k in range(j, N-i) :
            print(' ', end='')
    print('*')

