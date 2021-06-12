# 모듈이란?
# 특정 기능, 또는 이에 해당 하는 라이브러리
# 다수의 함수, 클래스 들로 구성될 수 있음

# 여러 함수, 클래스를 하나의 파일로 묶으면 그것이 모듈이다.
# Ex] myMod.py -> myMod

# 모듈 사용 : 모듈이 위치한 디렉토리
# 문법:
#   import 'name'
#   import 'name' as 'nickname'
#   from 'name' import 'function'
#   from 'name' import * or from 'name' import m_sum, m_div

# 패키지란?
# 여러 파이썬 모듈을 묶은 실행 가능한 애플리케이션이나 라이브러리를 말함
# Package > Module > Class > Function

# import time
# for i in range(10):
#     print(time.ctime()) # 현재시간
#     time.sleep(1)
# print(time.time()) # 협정 세계 표준시(UTC)

# import random
#
# count = 0
# n = 0
# total = 0
# for i in range(5):
#     while n < 1000000:
#         a = random.randint(1,6)
#         b = random.randint(1,6)
#         if a == b:
#             count += 1
#         n += 1
#     total += count/n
# print(total/5)
