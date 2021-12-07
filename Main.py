# http://dbcafe.co.kr/wiki/index.php/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EB%AA%85%EB%AA%85%EA%B7%9C%EC%B9%99
# 위의 주소는 파이썬 명명규칙 블로그입니다.
# ""는 텍스트, ''는 기호, 식별자, ""는 docstrings, 정규표현식로 규칙

# tkinter 임포트 합니다.
import tkinter


window = tkinter.Tk() # 선언합니다.
window.title("동영상 다운로더") # 제목 설정합니다.

# 너비, 높이, x, y의 좌표 선언합니다.
w = 900
h = 600
# sw = winfo_screenwidth()
# sh = winfo_screenheight()
# x = (sw - w) / 2
# y = (sh - h) / 2

window.geometry('%dx%d+%d+%d' %(w, h, 500, 500)) # geometry("너비x높이+x좌표+y좌표")
window.resizable(False, False)
# resizable(상하, 좌우)을 이용하여 윈도우 창의 창 크기 조절 가능 여부 설정,
# True로 설정하는 경우는 윈도우 창의 크기를 조절할 수 있습니다.

# 배경색 설정
window.configure(bg = "#79579e")

# 라벨 추가
label = tkinter.Label(window, text = "동영상 다운로더", width = 100, height = 5, fg="#ffffff", font = ("DotumChe", 30))
label.configure(bg = "#79579e")
label.pack()

# 버튼 추가
count = 0

def countUP():
    global count
    count += 1
    label.config(text = str(count))

label = tkinter.Label(window, text = "0")
label.pack()

button = tkinter.Button(window, text = "사이트 선택", overrelief = "flat", width = 100, height = 5, command = countUP, repeatdelay = 1000, repeatinterval = 100)
button.configure(bg="#ffffff")
button.pack(padx = 30, pady = 30)
button.pack()

button1 = tkinter.Button(window, text = "프로젝트 소개", overrelief = "flat", width = 100, height = 5, repeatdelay = 1000, repeatinterval = 100)
button1.configure(bg="#ffffff")
button1.pack(padx = 30, pady = 30)
button1.pack()

# 윈도우 창 뜨는 함수
window.mainloop()