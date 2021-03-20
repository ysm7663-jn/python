# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print('1번. q1 - ', len(q1))


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print('2번. \t',"apple;orange;banana;lemon")


# 3. 화면에 * 기호 100개를 표시하세요.

print('3-1번.')
for i in range(1, 101):
    print(i, ' : *')

print('3-2번', '*' * 100)
 

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
A = "30"
print('4번. 정수형:\t', type(int(A)), int(A))
print('     실수형:\t', type(float(A)), float(A))
print('     복소수형:\t', type(complex(A)), complex(A))
print('     문자형:\t', type(A), A)

print("4번")
print(int("30"))
print(float("30"))
print(complex("30"))
print(str(30))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

A = "Niceman"
print('5번. ', A[4:])

str = "Niceman"
manIdx = str.index("man") # index : 시작하는 단어(m)
print('5. 문자추출:\t', str[manIdx:manIdx + 3])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

q6 = "Strawberry"
print('6번. ', list(reversed(q6))) # ['y', 'r', 'r', 'e', 'b', 'w', 'a', 'r', 't', 'S']
print('6번. ', q6[::-1]) # yrrebwartS

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
q7 = "010-7777-9999"
print('7번.', q7.replace('-',''))
print('7번.', q7[0:3] + q7[4:8] + q7[9:])

# 정규표현식
import re
print('7번.', re.sub('[^0-9]', '', q7))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
q8 = "http://daum.net"
print('8번.', q8[7:])


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

print('9번.', "NiceMan".upper())
print('9번.', "NiceMan".lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
q10 = "abcdefghijklmn"
print('10번.', q10[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
q11 = ["Banana", "Apple", "Orange"]
del q11[1]
print('11번.', q11)
q11.insert(1, "Apple")
print(q11)
q11.remove("Apple")
print('11번.', q11)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)




# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>




# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.




# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.




# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.




# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
