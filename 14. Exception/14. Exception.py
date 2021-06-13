# 오류(error) 란?
# 프로그램 실행에서 발생할 수 있는 의도하지 않은 결과
# 오류는 프로그램 실행에 치명적 영향을 끼칠 수 있는 경우나, 단순히 원하지 않는 연산 결과를 낳기도 한다.
# 프로그램 실행시 발생하는 오류에 대해 프로그래머가 원하는 처리를 하고자 할 경우, 오류처리 구문을 사용할 수 있다.

# # 오류처리
# # 오류 발생 시, 처리할 코드를 정의함
# try:
#     정상 실행 코드
# except[발생 오류[as 오류 메시지 변수]]:
#     오류 발생시, 실행코드


# # 오류 처리 예
# def div(a, b):
#     try:
#         return a / b
#     except:
#         return "div error"
#
#
# print(div(4, 0))


# try: ... except: ...
# 오류 종류 상관없이 except 오류 처리

# try: ... except[발생오류]: ...
# 발생 오류가 지정된 오류와 일치할 경우

# # try: ... except[발생오류]as[오류 메시지 변수]:...
# # 발생 오류의 메시지를 확인[리턴] 받고싶을 경우
# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         return e
#
#
# print(div(4, 0))


# # try: ... except[오류타입1]:... except[오류타입2]:... except[오류타입 n]:...
# # 복수 오류발생 처리 구문 정의
# try:
#     4 / 0
#     a = [1, 2]
#     print(a[3])
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)


# # try: ... except(오류타입1, 오류타입2, ...)
# # 복수 오류발생 동시처리 구문
# try:
#     4 / 0  # division error
#     a = [1,2]
#     print(a[3]) # index error
# 처음으로 등장하는 오류를 return 한다.
# except (ZeroDivisionError, IndexError) as e:
#     print(e)


# try: ... except: ... else: ...
# 오류가 발생하지 않을 경우, else 구문 수행


# try: ... except[오류타입]: pass
# 오류 발생 시, 통과 pass


# # finally 처리
# # 오류 발생 시, 미처리 되는 중요한 코드에 대해 오류 처리 후 수행을 강제할 수 있다.
# # ex] 파일 닫기
# #     파일을 열어 놓고 사용 중에 오류가 발생할 경우 해당 파일을 닫아야 한다.
# with open('in.txt', 'w') as f:
#     try:
#         f.write('wonseok')
#         4 / 0
#     except FileNotFoundError as e:
#         print(e)
#     except ZeroDivisionError as e:
#         print(e)
#     finally:
#         print('exception occurs, file close')
#         f.close()
#
# try:
#     f = open('in.txt', 'r')
# except FileNotFoundError as e:
#     print(e)
# finally:
#     print(f.read(5))
#     f.close()
#     print('file close')


# class StudentNotFound(Exception):
#     def __str__(self):
#         return 'no such student'
#
#
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# s1 = [Student('kim', 98), Student('park', 88)]
# s = Student('park', 56)
#
# try:
#     if s not in s1:
#         raise StudentNotFound  # StudentNotFound 오류를 발생시킨다.
#     pass
# except StudentNotFound as e:  # StudentNotFound 오류가 발생되어 예외처리를 진행한다.
#     print(e)


# 사용자 Exception의 오류에 대한 처리
# 상속 오류 처리의 경우, super 클래스(Exception 혹은 바로 상위 클래스) 에서 동일하게 처리된다.
# 따라서 중복 오류처리가 필요한 경우, 동일한 super Exception일 경우 Except 구문을 중복 사용할 필요가 없다.
# 한 마디로, 최상위 클래스인 Exception을 상속받는 클래스들은 오류가 발생해도 Execption 에 포함되어 처리되기때문에 하나의 except 구문만 필요하다.


# class StudentNotFound(Exception):
#     def __str__(self):
#         return "no such student"
#
#
# class StudentDuplicated(Exception):
#     def __str__(self):
#         return "duplicated student"
#
#
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# s1 = [Student('kim', 98), Student('park', 88)]
# s = Student('park', 56)
#
# try:
#     if s not in s1:
#         raise StudentNotFound
#     for n in s1:
#         if s.name == n.name:
#             raise StudentDuplicated
# except Exception as e:
#     print(e)