import os
from tkinter import *

def find_file(event=None):
    file_name = entry.get()
    text.insert(END, "=====================" + '\n')
    text.insert(END, file_name + '\n')
    text.insert(END, "파일 찾기 시작!" + '\n')
    text.insert(END, "=====================" + '\n')
    for root, dirs, files in os.walk('C://'):
        for file in files:
            if file == file_name:
                text.insert(END, "파일을 찾았습니다." + '\n')
                text.insert(END, os.path.join(root, file) + '\n')
                return
    entry.delete(0,END)

def fn_delete():
    text.delete(1.0, END)

app = Tk()
app.geometry("400x300")
app.columnconfigure(0,weight=1)
app.rowconfigure(1, weight=1)

#엔트리.. 입력하는 부분
entry = Entry(app, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)
entry.bind("<Return>", add_text)

#텍스트..텍스트 위젯 부분
text = Text(app)
text.grid(row=1, column=0, columnspan=2)

btn = Button(app,text='추가', command=add_text)
btn.grid(row=0, column=1, padx=10, pady=10)

btn2 = Button(app, text='전체삭제', command=fn_delete)
btn2.grid(row=0, column=2)

app.mainloop()