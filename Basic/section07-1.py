# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스(객체), 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명 :   클래스명의 첫 글자는 대문자, 단어와 단어 사이는 대문자
#    함수
#    함수
#    함수

# 예제1

class UserInfo:
    # 속성, 메소드
    # 클래스 초기화 
    
    def __init__(self, name): 
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")

# 인스턴스 (네임스페이스)
user1 = UserInfo("Kim") # user1이란 인스턴스 생성
print(user1.name) # Kim
user2 = UserInfo("Park")
print(user2.name) # Park

# 별도의 메모리 공간 사용
print(id(user1)) # 1851124973040
print(id(user2)) # 1851124972944

user1.print_info() # Name : Kim
user2.print_info() # Name : Park

# 클래스 네임스페이스 확인
print('user1 : ', user1.__dict__) # user1 :  {'name': 'Kim'} 
print('user2 : ', user2.__dict__) # user2 :  {'name': 'Park'}


# 예제2
# self의 이해

class SelfTest:
    def function1(): # 클래스 메소드
        print("function1 called!")

    def function2(self): # 인스턴스 메소드
        print(id(self)) 
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f)) # 2623498783712
# f.function1() # 예외 발생
SelfTest.function1() # 클래스 메소드를 사용 : 클래스.메소드 function1 called!
f.function2() # 인스턴스 메소드 사용 : 2623498783712 function2 called!
print(SelfTest.function1()) # function1 called!

# print(SelfTest.function2()) # 예외 발생


# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    # 클래스 변수 / self 없음 / 여러 인스턴스에서 공유
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Kim')
user2 = Warehouse('Park')
user3 = Warehouse('Lee')

print(user1.name) # Kim
print(user2.name) # Park
print(user3.name) # Lee
print(user1.__dict__) # {'name': 'Kim'}
print(user2.__dict__) # {'name': 'Park'}
print(user3.__dict__) # {'name': 'Lee'}
print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# Warehouse.stock_num = 50 # 직접 접근 가능

# 자기 네임스페이스에 변수가 없으면, 클래스 네임스페이스에 있는 변수를 찾아 출력 / 클래스 변수도 없을 경우 오류 발생
print(user1.stock_num) # 3
print(user2.stock_num) # 3
print(user3.stock_num) # 3

del user1

print(user2.stock_num) # 2
print(user3.stock_num) # 2