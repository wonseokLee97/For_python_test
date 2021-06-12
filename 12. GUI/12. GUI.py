# GUI 란? // Graphic User Interface 의 약자
# 대표적으로 window, tk 등이 존재
# 윈도우 프레임, 버튼, 창 등 위젯으로 사용자 환경 구현

# 파이썬 GUI 구현
# tkinter(TK 인터페이스) 모듈을 이용한 GUI 구현
# 다양한 위젯 사용 (버튼, 캔버스, 프레임, 레이블, 박스, 스크롤바 등등)
# 이벤트(사용자 입력) 핸들러 구현

# wxPython : C++로 작성된 크로스 플랫폼 GUI 툴인
# wxWidgets를 파이썬에서 이용할 수 있게 한다.
#
# PyQT: TKintner나 기타 다른 툴보다 쉽고 예쁜 인터페이스를
# 가진 GUI 편집기인 QT Designer을 사용할 수 있는 것이 장점이다.
#
# Kivy: 멀티터치 지원이 강점. OpenGL ES2로 GUI 환경 구현하므로
# 스마트폰에서도 구현 가능하다. 동일한 코드로 여러 환경에서 동일한
# 인터페이스를 구현할 수 있고 프로그래밍 시간도 짧다.
#
# PyGame: 파이썬으로 비디오 게임을 제작하기 위한 프레임워크이다.
# 게임을 만들지 않아도 캔버스와 그래픽 그리기, 다채널 사운드 처리 등의
# 여러 동작을 복잡 하지 않게다룰 수 있다.
# 그러나 PyGame이 제공하는 기능을 적용하지 못하는 환경이 있을 수 있다.


# # tinker 모듈에서 생성자 Tk()를 이용하여 인스턴스(참조자) 생성
# # window main loop 실행
# import tkinter as tk
#
# # 도화지 생성
# window = tk.Tk()


# # Label - 텍스트, 이미지 표시
# lb1 = tk.Label(window, text='id')
# # Entry - 입력 받을 수 있는 한 줄의 텍스트
# e1 = tk.Entry(window)
# # Grid 를 활용하여 배치
# lb1.grid(row=0, column=0)
# e1.grid(row=0, column=1)
#
# lb2 = tk.Label(window, text='pw')
# e2 = tk.Entry(window)
# lb2.grid(row=1, column=0)
# e2.grid(row=1, column=1)
#
# bn1 = tk.Button(window, text='login')
# bn1.grid(row=2, column=1)
# window.mainloop()


# # 이벤트 (Event) 란?
# # 이벤트 발생 시, 해당 이벤트를 큐 (Queue) 에 넣어 순서대로 처리한다.
# # 이벤트는 이벤트 이름, 이벤트에 관한 데이터, 이벤트를 처리하는 함수 등의
# # 정보로 구성되어 있음
# # 이벤트 핸들러는 해당 이벤트를 큐에서 꺼내어, 이벤트 처리를 위한 함수에게 던져준다.
# #
# # 이벤트 실습] 섭씨, 화씨 온도 변환
#
# def CtoF():
#     # e2에 입력된 섭씨를 화씨로 변환하여,
#     val = int(e2.get()) * 9 / 5 + 32
#     # e1에 입력된 화씨값을 지우고
#     e1.delete(0, 10)
#     # e1에 변환된[섭씨 -> 화씨] 값을 삽입한다.
#     e1.insert(0, str(val))
#
#
# def FtoC():
#     # e1에 입력된 화씨를 섭씨로 변환하여,
#     val = (int(e1.get()) - 32) * 5 / 9
#     # e2에 입력된 섭씨값을 지우고
#     e2.delete(0, 10)
#     # e2에 변환된[화씨 -> 섭씨] 값을 삽입한다.
#     e2.insert(0, str(val))
#
#
# lb1 = tk.Label(window, text='화씨')
# e1 = tk.Entry(window)
# lb1.grid(row=0, column=0)
# e1.grid(row=0, column=1)
#
# lb2 = tk.Label(window, text='섭씨')
# e2 = tk.Entry(window)
# lb2.grid(row=1, column=0)
# e2.grid(row=1, column=1)
#
# bn1 = tk.Button(window, text='섭씨->화씨', command=CtoF)
# bn1.grid(row=2, column=0)
# bn2 = tk.Button(window, text='화씨->섭씨', command=FtoC)
# bn2.grid(row=2, column=1)
# window.mainloop()


# # 이벤트 핸들러 바인딩
# def mouseEvHandler(event):
#     print('click at ', event.x, event.y)
#
#
# frame = tk.Frame(window, width=300, height=300)
# frame.bind('<Button-1>', mouseEvHandler)
# frame.pack
#
# window.mainloop()


# HW

import tkinter as tk

window = tk.Tk()


def getName():
    value = e1.get()
    print('내 이름은 ', value, ' 입니다.')


lb1 = tk.Label(window, text='이름')
e1 = tk.Entry(window)
lb1.grid(row=0, column=0)
e1.grid(row=0, column=1)

btn = tk.Button(window, text='OK', command=getName)
btn.grid(row=1, column=1)

window.mainloop()