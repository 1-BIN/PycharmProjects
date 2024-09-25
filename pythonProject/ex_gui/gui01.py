from tkinter import *
from tkinter import messagebox
from python_base.luck import make_lotto3


app = Tk()
app.geometry("200x100")
app.title('로또번호 생성기')
def get_lotto():
    msg = txt.get()     #entry 값을 가져옵니다.
    lottoes = []
    for i in range(int(msg)):
        lottoes.append(make_lotto3())
    messagebox.showinfo('생성완료', str(lottoes))        ## alert같은 역할입니다.

lbl = Label(app, text='수량')
lbl.grid(row=0, column=0, padx=10, pady=10)
txt = Entry(app)
txt.grid(row=0, column=1, padx=10, pady=10)
btn = Button(app, text='생성', command=get_lotto)
btn.grid(row=1, column=0, columnspan=2, sticky = 'ew', padx=10, pady=10)
app.mainloop()

# exe파일로 만들기~!
# pip install pyinstaller
# pyinstaller --onefile -w (파일명 ex gui01.py)
# --onefile 하나의 파일로 생성
# --windowed or -w 콘솔 창 없이 gui 실행