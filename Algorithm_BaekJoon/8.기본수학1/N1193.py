N = int(input())

line = 1
# 이유 모름
while N > line :
    N = N - line
    line = line + 1

if line % 2 == 0 :
    a = N
    b = line - N + 1
else :
    a = line - N + 1
    b = N

print(a, '/', b, sep='')

