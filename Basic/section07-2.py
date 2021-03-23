# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

class Car:
    """Parent Class""" # 정의 
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        # print('Car Class "Show" Method!')
        return 'Car Class "Show" Method!'


class BmwCar(Car): # (부모 클래스) : 부모의 속성과 메소드를 모두 사용 가능
    """Sub Class"""
    
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모 메소드가 가지고 있는 속성을 부모에 보냄
        self.car_name = car_name # 자신의 고유 메소드

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        print(super().show()) # 부모 클래스에 존재하는 메소드를 그대로 사용
        return 'Car Info : %s %s %s' % (self.car_name, self.color,self.type)

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # Super / red
print(model1.type)  # Super / sedan
print(model1.car_name)  # Sub / 520d
print(model1.show())  # Super / Car Class "Show" Method! / 자신의 클래스에 없는 메소드여도 부모 클래스에 존재하는 메소드면 실행이 가능하다.
print(model1.show_model())  # Sub / Your Car Name : 520d
print(model1.__dict__) # {'type': 'sedan', 'color': 'red', 'car_name': '520d'}

# Method Overriding
# 부모 클래스에 존재하는 메소드지만 같은 이름의 메소드를 자신이 필요한 정보로 사용할 수 있다 / 부모 메소드와 매개변수가 동일해야됨
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show()) # Car Info : 220d black suv

# Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show()) # Car Class "Show" Method! Car Info : 350s silver sedan

# Inheritance Info (상속 관계 정보를 리스트 형태로 출력)
# 모든 클래스는 object를 상속 받는다.
print('Inheritance Info : ', BmwCar.mro()) # Inheritance Info :  [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
print('Inheritance Info : ', BenzCar.mro()) # Inheritance Info :  [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro()) # [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
print(A.mro()) # [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]