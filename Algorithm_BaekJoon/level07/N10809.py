strArr = input()

alpha = list(range(97, 123))

for i in alpha :
    print(strArr.find(chr(i)), end=' ')

print()

# .find() : 해당 값이 있는 인덱스 번호를 반환
# str = 'abcabc'
# print(str.find('b')) # 1