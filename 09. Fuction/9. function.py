# 함수란?
# 특정 기능을 수행하기 위해 작성된 코드 몫
# 함수는 특정 기능을 위해 입력 argument를 받고 결과값을 return 한다.

# 함수 호출의 예
# X = func_name(arg1, arg2)
# X = get_results(*args) , 여러 개 입력값
# X, Y = get_result() , 출력 값이 여러개인 경우 (튜플)

# ex]
# def sum_many(*args):
#     sum = 0
#     print(type(args))
#     for i in args:
#         sum += i
#     return sum
#
#
# print(sum_many(1, 2, 3, 4, 5))

# def sum_and_mul(a, b):
#     return a + b, a * b
# x, y = sum_and_mul(1, 2)
# print(x, y)

# def myrange(start, end, inc):
#     t1 = []
#     while start <= end:
#         t1.append(start)
#         start += inc
#     return t1
#
#
# print(myrange(0, 5, 1))

# def sum_to_list(a, b):
#     sum = 0
#     for x in a:
#         sum += x
#     for x in b:
#         sum += x
#     return sum
#
#
# print(sum_to_list([1, 2, 3], (1, 2, 3)))

# *args 경우, 각 입력값은 (튜플) 인덱스에 의해 접근
# **agrs 경우, 각 입력값은 (딕셔너리) 키에 의해 접근

# def sum_dic(**arg):
#     print(arg)
#     sum = 0
#     for x in arg.keys():
#         sum += arg[x]
#     return sum
#
#
# print(sum_dic(a=2, b=3, c=4))

# default 입력값
# def getNum(a=1, b=False):
#     if b:
#         return a
#
#
# print(getNum(1, 0))
# print(getNum(2, 1))
# print(getNum(3))
# print(getNum(True, True))

# 내장함수
# # abs() 절대값 반환
# print(abs(-10))
# # all() 모든 요소가 True 이면 True
# print(all((1,2,3)))
# # any() 어느 요소만 True 이면 True
# # bool(x) x의 boolean 값을 반환
# print(bool(""))
# # chr(숫자) 아스키 코드에 해당하는 문자를 반환
# print(chr(65))
# ord(문자) 해당 문자의 아스키 코드값 반환
# print(ord('A'))
# # dir([1,2]) 해당 객체(여기선 리스트)가 가진 변수, 메소드를 출력
# print(dir((1,2)))
# # enumerate(자료구조) 자료구조의 (요소번호, 요소) 튜플의 자료구조인 객체를 반환
# for i, ss in enumerate({'key1': 'a', 1: 'b', 2: 'c'}):
#     print(i, 'is', ss)
# 딕셔너리의 경우 키 값을 요소값으로 가져옴

# 클로저

# def out_func(a):
#     x = [0]
#     x[0] = a
#
#     def inner_func():
#         x[0] += a
#         return x[0]
#
#     return inner_func
#
# a = out_func(3)
# print(a())
# print(a())

# def calc():
#     a = 3
#     b = 5
#
#     def mul_add(x):
#         return a * x + b  # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
#
#     return mul_add  # mul_add 함수를 반환
#
#
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))

# lambda, map

# m = list(map(lambda x: x ** 2, [1,2,3,4]))
# print(m)
#
# a = list(map(int, input().split()))
# print(a)

# filter
# f = list(filter(lambda x : x-10, range(11)))
# print(f)

# def outer_func(*tup):
#     sum_ = sum(tup)
#
#     def inner_func(arg):
#         return sum_ + arg
#     return inner_func

# a = outer_func(1, 2, 3, 4)
# print(a(3))

