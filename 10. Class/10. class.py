# # 기본적인 클래스 형태
# class Car:
#     cc = 2000
#     seats = 4
#     speed = 0

# # 인스턴스 생성
# myCar = Car()  #객체 참조자
# print(type(myCar))

# # 클래스 속성에 접근
# myCar.cc = 1000
# print(myCar.cc)

# # 동적 속성 정의
# myCar.color = 'red'
# print(myCar.color)

# # 클래스 메소드 정의
# class Car:
#     cc = 2000
#     seats = 4
#     speed = 0
#
#     # self는 객체 자신의 주소값이다
#     def drive(self):
#         self.speed += 60

# # 데이터 접근 제한
# class Car:
#     cc = 2000
#     seats = 4
#     __color = 'red'
#
#     # 클래스 초기화
#     def __init__(self, speed, color, model):
#         self.__speed = speed
#         self.__color = color
#         self.model = model
#
#     def drive(self):
#         self.__speed = 60
#
#     # 접근자 메소드
#     def getSpeed(self):
#         return self.__speed
#
#     def getColor(self):
#         return self.__color
#
#     # 변형자 메소드
#     def setColor(self, c):
#         self.__color = c
#
#
# myCar = Car(30,'red','avante')
# myCar.drive()
# myCar.setColor('blue')
# print(myCar.seats)
# print(myCar.getColor())

# # 클래스 초기화
# class wonseok:
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
#
# aboutme = wonseok(25, 180)
# print(aboutme.age)

# # 상속
# class Vehicle():
#     def __init__(self, speed, color='white'):
#         self.speed = speed
#         self.color = color
#
#
# class Car(Vehicle):
#     def __init__(self, speed, color, wheels, seats):
#         # super() 메소드를 통해 상위 클래스를 초기화 시킨다
#         super().__init__(speed, color)
#         self.wheel = wheels
#         self.seats = seats
#
#
# class Sport(Car):
#     def __init__(self, speed, wheel, seats, color='white', turbo=True, conv=False):
#         # super() 메소드를 통해 상위 클래스를 초기화 시킨다
#         super().__init__(speed, color, wheel, seats)
#         self.turbo = turbo
#         self.conv = conv
#
# mySport = Sport(40, 4, 4)
# print(mySport.speed)

# # 오버라이딩
# # 상위 클래스의 메소드를 하위 클래스에서 재 정의하여 사용한다.
#
# class A:
#     def sayHi(self):
#         print('I am A')
#
#
# class B(A):
#     def sayHi(self):
#         print('I am B')
#
## 연속적으로 상속한 경우, 가장 마지막에 상속한 상위 클래스의 메소드를 호출출# class C(B):
#     pass
#
# a = A()
# b = B()
#
# a.sayHi()
# b.sayHi()

# # 다중 상속 // 다수 클래스로부터 상속
# class A:
#     def sayHi(self):
#         print('I am A')
#
#
# class B:
#     def sayHi(self):
#         print('I am B')
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# print(C.mro())
# c.sayHi()

# # 연산자 오버라이딩
# class Complex:
#     def __init__(self, r, i):
#         self.re = r
#         self.im = i
#
#     def __add__(self, other):
#         c = Complex(self.re + other.re, self.im + other.im)
#         return c
#
#     def __str__(self):
#         return  str(self.re) + '+' + str(self.im) + 'i'
#
#
# result = Complex(2, 3) + Complex(3, 4)
# print(result)

# class Shape:
#     def __init__(self, a):
#         self.area = a
#
#     def __gt__(self, other):
#         print(self.area, other.area)
#         return self.area > other.area
#
#
# class Circle(Shape):
#     PI = 3.14
#
#     def __init__(self, r):
#         super().__init__(r ** 2 * Circle.PI)
#
#
# class Rect(Shape):
#     def __init__(self, w, h):
#         super().__init__(h * w)
#
#
# c = Circle(2)
# r = Rect(2, 3)
# print('Rect is Bigger' if c < r else 'Circle is Bigger')
# print(c < r)
# print(c > r)

# 클래스 변수와 인스턴스 변수의 차이
# 인스턴스 변수 : 객체가 생성되었을 때, 객체가 가지는 개별 고유의 변수
# 클래스 변수 : 객체가 아닌 클래스가 가지는 변수
# 접근법 //
# 클래스 변수 : Classname.var or method
# 인스턴스 변수 : Objectname.var or method

# class TV:
#     serialNum = 0
#
#     def __init__(self):
#         TV.serialNum += 1
#         self.serialNum = TV.serialNum
#
#
# a = TV()
# b = TV()
# print(a.serialNum, b.serialNum, TV.serialNum)

# 클래스 메소드
# 클래스 메소드는 객체가 아닌 클래스에 정의된 함수이다.
# 따라스 클래스 메소드는 self를 입력 변수로 주지 않는다.

# class A:
#     a = 10
#
#     def getA():
#         return A.a
#
# print(A.getA())

# class A:
#     n = 10
#
#     def setA():  # 클래스 메소드
#         A.n += 1

# a = A()
# A.setA()
# print(a.n, A.n) 11, 11
# a라는 인스턴스에 따로 인스턴스 변수를 가지고있지 않기에,
# 클래스 A의 클래스 변수 n을 계승하여 사용한다.

# a = A()
# a.n = 10
# A.setA()
# print(a.n, A.n) 10 11
# a라는 인스턴스에 변수가 사용되어, 인스턴스 변수 n에 접근한다.

# 클래스 변수 은닉
# private 변수를 선언하면 클래스 메소드를 통해서만 접근 가능하다.
# 또한 클래스 메소드는 인스턴스 변수에 접근할 수 없다.
# class A:
#     __n = 1
#     def setA():
#         A.__n += 1
#     def getA():
#         return A.__n
#
# A.setA()
# print(A.getA())

# class A:
#     def __init__(self):
#         self.__n = 10
#
#     def setA(self):
#         self.__n += 1
#
# a = A()
# a.setA()

# # HW
# class Car:
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
#     def setSpeed(self, setSpeed):
#         self.speed += setSpeed
#
#     def getSpeed(self):
#         return self.speed
#
#
# class Sport(Car):
#     def __init__(self, color, speed, seats):
#         # 색상, 속도를 Car 로 부터 상속받는다.
#         super().__init__(color, speed)
#         self.seats = seats
#
#     def getSeats(self):
#         return self.seats
#
#     # 속도 변경을 Car 로 부터 상속받는다.
#
#
# class Truck(Car):
#     def __init__(self, color, speed, weight):
#         # 색상 속도를 Car 로 부터 상속받는다.
#         super().__init__(color, speed)
#         self.weight = weight
#
#     def getWeight(self):
#         return self.weight
#
#     # 속도 변경을 Car 로 부터 상속받는다.
#
#
# mySport = Sport('red', 20, 4)
# myTruck = Truck('white', 20, 100)
#
# myTruck.setSpeed(50)
# print('Truck speed :', myTruck.getSpeed())
# print('Car speed :', mySport.getSpeed())
