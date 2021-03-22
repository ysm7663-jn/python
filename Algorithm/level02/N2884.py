h, m = map(int, input().split())

if h == 0 and m < 45:
    h = 23
    m += 15
elif h > 0 and m < 45:
    h -= 1
    m += 15
else :
    m -= 45

print(h , m)
