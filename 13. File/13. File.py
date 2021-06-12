# File 이란?
# 프로그램 종료에 따라 사용하던 데이터는 메모리에서 삭제
# 따라서 작업한 데이터를 저장하고 프로그램 재실행 시에, 복원하기 위해서
# 파일에 저장해 2차 저장 공간인 디스크에 기록해야 한다.

# 파일은 보조 기억 장치에서 문서, 소리, 그림, 영상 등의 자료를 저장
# 관리하는 시스템으로 프로그래머 및 사용자에게 논리적 인터페이스를 제공한다.

# 파일 시스템의 구성 // 디렉토리, 파일
# 파일의 종류
# - 텍스트 파일 : 사람이 읽고 쓸 수 있는 텍스트가 있는 파일.
#              아스키/ 유니 코드로 저장되어 있고 연속적인 line 으로 구성된다.
# - 이진 파일 : 0 과 1로 이루어진 데이터파일로 사람이 직접 읽을 수 없다.
#             따라서 line 의 의미가 없다.

# 파일 읽기 순서
# 파일 열기 -> 파일 읽기 -> 파일 닫기
# # Ex]
# fh = open('file path', 'r') # 읽기
# Lines = fh.read() # 전체 읽기
# Line = fh.readline() # line 읽기
# fh.close()


# # 파일을 읽고 프린트 하시오.
# infile = open('in.txt', 'r')
# print(infile.read())  # 파일 전체 read
# print('\n')
# infile.seek(0)  # 커서를 파일의 첫 번째 줄로 옮긴다. / 초기화
# print(infile.readline()) # 첫 번째 줄 read
# print(infile.readline()) # 두 번째 줄 read
# print(infile.readline()) # 세 번째 줄 read
# infile.seek(0)
# print(infile.readlines()) # 모든 줄 read


# with 를 이용한 파일 열기
# with open(파일이름, 쓰기 or 읽기) as 파일핸들러[파일]:
# 파일핸들러[참조자] 를 사용하는 코드 블럭으로 구분
# 코드 블럭을 종료 시, 해당 파일 자동 close 된다.(cloes() 메소드 생략)
# with open('in.txt', 'r') as infile:
#     s = infile.read(7) # 7번째 단어까지 read
#     print(s)
#     print(infile.tell()) # infile 에서 현재 위치 return


# # 파일 생성
# # 쓰기 파일이 없을 경우, 파일 생성
# fh = open('test.txt', 'w')
# # a : append(추가하다), 'w' 파일 덮어 쓰기, 'r' 파일 읽기
# fh.write('hizz\n')
# fh.write('python')
# fh.close()


# # 터미널로 파일 쓰기
# # 명령 실행 옵션으로 넘겨준 정보들은 sys의 배열 인자에 담김
# import sys
# option = sys.argv[1]
#
# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt', 'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()
#     print('memo is saved')


# pickle 모듈
# 자료구조[리스트, 딕셔너리, 튜플 등]를 binary 이진 파일로 저장하고 불러올 수 있다.
# 텍스트 파일 저장에 비해 사용이 편리하고, 잘구조의 저장과 복구가 쉽다.
# 문법
# import pickle
# pickle.dump('자료구조', 파일 참조자)
# pickle.load('파일 참조자')

# # pickle 을 사용하여 list 자료구조 저장
# import pickle as pk
#
# s1 = [('kim', 89), ('lee', 90), ('park', 77)]
#
# with open('db.txt', 'wb') as f:
#     pk.dump(s1, f)
#
# print(pk.load(open('db.txt', 'rb')))


# # HW
# import pickle as pk
#
# id = input('아이디를 입력하세요 : ')
# pw = input('비밀번호를 입력하세요 : ')
#
# account = {id: pw}
#
# with open('account.txt', 'wb') as f:
#     pk.dump(account, f) # 자료구조 account 를 byte 형태로 f에 write 하여 저장한다.
#
# with open('account.txt', 'rb') as f:
#     data = pk.load(f)
#
# print(data)
#
# print(pk.load(open('account.txt', 'rb')))