# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

#기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

# 문자열 출력에는 '', "", ''' ''', """ """ 사용 가능

print()
# print 함수에 입력값이 없을 경우 줄바꿈 역할

# Separator 옵션 사용

print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')

print('2021', '03', '16') 
print('2021', '03', '16', sep='-')

print('niceman', 'google.com')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
# 끝을 내지 않으므로 뒤의 것과 이어준다.
print('Welcome To ', end='')
print('the blue paradies', end=' ') # end 옵션이 있으므로 뒤에 오는 print문에 줄바꿈이 이뤄지지 않는다.
print('piano notes') # end 옵션이 없으므로 줄바꿈이 이뤄진다.
print('test')

print()

# format 옵션
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Kim', 7))

print()

print("Test1 : %5d, price : %4.2f" %(776, 6534.123))
print("Test1 : {0: 5d}, price :{1: 4.2f}".format(776,6534.123))
print("Test1 : {a: 5d}, price :{b: 4.2f}".format(a=776, b=6534.123))

print()

# \ : 이스케이프 문자
# \t : 탭 (스페이스 4번)
# \n : 줄바꿈
# \', \", \\ : ', ", \ 출력
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\t\t\ttest') 


