# 데이터 타입

v_str1 = "Nice man"
v_boolean = True
v_str2 = "Good Boy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_float))
print(type(v_tuple))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10
print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)
print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
y += 100
print(y)

# 절대값
print(abs(-7))

# 몫, 나머지를 각각 나눠줌
n, m = divmod(100, 8)
print(n, m)

import math
# (n) 의 수보다 큰 정수중 가장 작은 정수
print(math.ceil(5.1))
# (n) 의 수보다 작은 정수중 가장 큰 정수
print(math.floor(3.874))

