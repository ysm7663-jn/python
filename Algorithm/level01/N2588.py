a = int(input())
b = int(input())

b_baek = int(b / 100)
b_ship = int((b % 100) / 10)
b_ill = b % 10

print(a * b_ill, a * b_ship, a * b_baek, a*b, sep='\n')