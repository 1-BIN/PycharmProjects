from tkinter import *

def add_text(event=None):
    user_input = entry.get()
    text.insert(END, user_input + '\n')
    entry.delete(0,END)

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

def fn_delete():
    text.delete(1.0, END)

btn2 = Button(app, text='전체삭제', command=fn_delete)
btn2.grid(row=0, column=2)

app.mainloop()