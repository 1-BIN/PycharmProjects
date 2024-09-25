import tkinter as tk
from tkinter import scrolledtext
from crawling import get_img
import threading

def search_data():
    # 입력 검색어
    search_query = entry.get()
    # 내용출력
    txt.configure(state='normal') # 입력 가능한 상태
    txt.delete(1.0, tk.END) # 기존 내용 지우기
    line = "=" * 40
    txt.insert(tk.INSERT, line + "\n")
    txt.insert(tk.INSERT, search_query + " 이미지\n")
    txt.insert(tk.INSERT, "수집을 시작합니다.\n")
    txt.insert(tk.INSERT, line + "\n")
    txt.insert(tk.INSERT, "\n")
    def fetch_images(): #스레드 사용을 위해 함수를 만들어줍니다.
        all_size, del_size = get_img(search_query)
        txt.insert(tk.INSERT, "관련 이미지 수: " + str(all_size) + "\n")
        txt.insert(tk.INSERT, "삭제 이미지 수: " + str(del_size) + "\n")
        txt.insert(tk.INSERT, "저장 이미지 수: " + str(all_size-del_size) + "\n")
        txt.insert(tk.INSERT, line + "\n")
        txt.insert(tk.INSERT, "수집 종료.\n")
        txt.configure(state='disabled')  # 편집 불가능 상태

    threading.Thread(target=fetch_images).start()   #스레드 설정을 해줍니다.


app = tk.Tk()
app.title("이미지 검색 수집기")
# 창 크기 변경 X
app.resizable(False, False)
# 검색어 입력
lab = tk.Label(app, text='검색어')
lab.pack()
entry = tk.Entry(app)
entry.pack()
btn = tk.Button(app, text='수집', command=search_data)
btn.pack()
# 스크롤 가능한 텍스트 영역
txt = scrolledtext.ScrolledText(app, width=40, height=20
                                , state='disabled')
txt.pack()
app.mainloop()