# Section04-2
# 파이썬 데이터 타입(자료형)
# 문자열, 문자열 연산, 슬라이싱
# 문자열 중요성(가장 많은 분야에서 사용)

# 문자열 생성
str1 = "I am Boy."
str2 = 'NiceMan'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(str1)
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
# 빈 칸과 특수 기호도  포함

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'

# 출력1
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

# 탭, 줄바꿈
t_s1 = "Tab \tClick!"
t_s2 = "New Line\n Start!!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
# 경로 작성때 주로 사용, 있는 그대로 출력
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1) # NicemanNicemanNiceman
print(str_o1 + str_o2) # NicemanOrange
print(dir(str_o1))
print('x' in str_o1) # False
print('i' in str_o1) # True
print('e' not in str_o2) # False
print('O' not in str_o2) # False

# 문자열 형 변환

# print(3 + str_o1) 은 불가, *는 반복으로 받아들인다
print(str(77) + 'a')  # type 확인, 문자형 / 77a
print(str(77))  # type 확인, 문자형 / 77
print(str(10.4)) # 문자형 / 10.4
print(str(True)) # True
print(str(complex(12))) # (12+0j)

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print("Capitalize: ", str_o1.capitalize())  # 첫 글자를 대문자로 바꿈
print("endswith?: ", str_o2.endswith("s"))  # 맨 끝 글자가 "s" 냐? True, False 반환
print("join str: ", str_o1.join(["I'm ", "!"])) # join str:  I'm Niceman!
print("replace1: ", str_o1.replace('Nice', 'Good')) # 앞에 글자를 뒤에 글자로 대체
print("replace2: ", str_o3.replace("is", "was", 3)) # replace2:  thwas was string example....wow!!! thwas is really string
print("split: ", str_o4.split(' '))  # Type 확인 / 띄어쓰기 마다 구분 지음
print("sorted: ", sorted(str_o1))  # reverse=True   / 
print("reversed1: ", reversed(str_o2)) #list 형 변환  
print("reversed2: ", list(reversed(str_o2)))    # 리스트에 들어있는 단어들을 역순으로 출력

# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# 출력
for i in im_str:
    print(i)

# im_str[0] = "T"  # 수정 불가(immutable)

# 슬라이싱(인덱싱)
# 역순은 오른쪽부터 -1
# 끝에 수 -1까지
# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[:len(str_sl)]) # 0 ~ 6
print(str_sl[:len(str_sl) - 1]) # 0 ~ 5
print(str_sl[:])    # 처음부터 끝까지
print(str_sl[1:4:2])    # 1번부터 3번까지중 2개씩 출력
print(str_sl[-3:6]) # -3:b ~ 6:o // ie
print(str_sl[1:-2]) # 1:i ~ -2:o // iceb
print(str_sl[::-1]) # 처음부터 끝까지, -1:역순으로
print(str_sl[::2])  # N, c, b, y

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a))
print(chr(116))
