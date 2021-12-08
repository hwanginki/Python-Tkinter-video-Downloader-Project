# http://dbcafe.co.kr/wiki/index.php/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EB%AA%85%EB%AA%85%EA%B7%9C%EC%B9%99
# 위의 주소는 파이썬 명명규칙 블로그입니다.
# ""는 텍스트, ''는 기호, 식별자, ""는 docstrings, 정규표현식로 규칙

# tkinter 임포트 합니다.
import tkinter
import tkinter.ttk # 이거 왜 추가해야되는 이유는 모르겠다. 아마도 콤보박스 관련 라이브러리라서 그런가

window = tkinter.Tk() # Tk()이용하여 윈도우 창을 생성합니다.
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
label = tkinter.Label(window, text = "동영상 다운로더", width = 100, height = 5, fg = "#ffffff", font = ("DotumChe", 30))
label.configure(bg = "#79579e")
label.pack()

# 버튼 추가
count = 0

def countUP():
    global count
    count += 1
    label.config(text = str(count))

def self_window():
    self_window = tkinter.Tk()
    self_window.title("프로젝트 소개")
    w = 500
    h = 500
    self_window.geometry('%dx%d+%d+%d' %(w, h, 500, 500))
    self_window.resizable(False, False)
    self_window.configure(bg = "#79579e")

def select_window():
    window = tkinter.Tk()
    window.title("사이트 선택")
    w = 900
    h = 500
    window.geometry('%dx%d+%d+%d' %(w, h, 500, 500))
    window.resizable(False, False)
    window.configure(bg = "#79579e")

    self_label = tkinter.Label(window, text = "사이트 선택", width = 100, height = 5, fg = "#ffffff", font = ("DotumChe", 30))
    self_label.configure(bg = "#79579e")
    self_label.pack()

    # 여기서 판다스로 엑셀 파일 읽어불러오기 로직넣는 부분
    values = ["네이버", "다음", "유튜브"]
    # end

    combobox=tkinter.ttk.Combobox(window, values = values)
    combobox.set("유튜브")
    combobox.pack()

    button2 = tkinter.Button(window, text = "이동", overrelief = "flat", width = 100, height = 5, command = downlode_window, repeatdelay = 1000, repeatinterval = 100)
    button2.configure(bg = "#c4df9b")
    button2.pack(padx = 50, pady = 100)
    button2.pack()

def downlode_window():
    window = tkinter.Tk()
    window.title("다운로드")
    w = 900
    h = 500
    window.geometry('%dx%d+%d+%d' %(w, h, 500, 500))
    window.resizable(False, False)
    window.configure(bg = "#79579e")
    
    # 콤보박스에서 값을 선택하면 그 라벨이 수정할 수 있도록 고칠 것
    downlode_label = tkinter.Label(window, text = "유튜브", width = 100, height = 4, fg = "#ffffff", font = ("DotumChe", 30))
    downlode_label.configure(bg = "#79579e")
    downlode_label.pack()

    # place() 위젯 배치에 x, y축 설정하여 사용합니다.
    downlode_label = tkinter.Label(window, text = "동영상 UTL", width = 10, height = 5, fg = "#ffffff", font = ("DotumChe", 15))
    downlode_label.configure(bg = "#79579e")
    downlode_label.place(x = 50, y = 90)
    
    downlode_label = tkinter.Label(window, text = "동영상 품질", width = 10, fg = "#ffffff", font = ("DotumChe", 15))
    downlode_label.configure(bg = "#79579e")
    downlode_label.place(x = 50, y = 200)
    
    downlode_label = tkinter.Label(window, text = "저장경로", width = 10, fg = "#ffffff", font = ("DotumChe", 15))
    downlode_label.configure(bg = "#79579e")
    downlode_label.place(x = 50, y = 265)

    # 입력하고 엔터하면 라벨에서 출력하는 로직
    def calc(event):
        label.config(text = "결과 = " + str(eval(entry.get())))

    entry = tkinter.Entry(window, width = 82)
    # bind() 이용해 함수를 쓰면 될 듯?!
    entry.bind("<Return>", calc)
    entry.place(x = 200, y = 135)

    label = tkinter.Label(window)
    label.place(x = 200, y = 100)

    entry = tkinter.Entry(window, width = 70)
    entry.place(x = 200, y = 270)
    
    # 품질 콤보박스 값 추가
    quality_lists = ["2160p(4K)", "1440p(HD)", "1080p(HD)", "720p", "480p", "360p", "240p", "144p"]
    combobox = tkinter.ttk.Combobox(window, values = quality_lists, width = 80)
    combobox.set("품질 선택")
    combobox.place(x = 200, y = 200)

    button3 = tkinter.Button(window, text = "다운로드", overrelief = "flat", width = 100, height = 3, repeatdelay = 1000, repeatinterval = 100)
    button3.configure(bg = "#c4df9b")
    button3.place(x = 110, y = 350)

    downlode_label = tkinter.Label(window, text = "다운로드 횟수 : ", width = 20, fg = "#ffffff", font = ("DotumChe", 15))
    downlode_label.configure(bg = "#79579e")
    downlode_label.place(x = 150, y = 430)

label = tkinter.Label(window, text = "0")
label.pack()

button = tkinter.Button(window, text = "사이트 선택", overrelief = "flat", width = 100, height = 5, command = select_window, repeatdelay = 1000, repeatinterval = 100)
button.configure(bg = "#ffffff")
button.pack(padx = 30, pady = 30)
button.pack()
 
button1 = tkinter.Button(text = "프로젝트 소개", overrelief = "flat", width = 100, height = 5, command = downlode_window, repeatdelay = 1000, repeatinterval = 100)
button1.configure(bg="#ffffff")
button1.pack(padx = 30, pady = 30)
button1.pack()

# 윈도우 창 뜨는 함수
window.mainloop()