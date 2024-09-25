import tkinter as tk
import time
import threading

def long_task():
    time.sleep(5)   #해당 작업이 오래걸리기 때문에, 스레드를 만들어줍니다.
    label.config(text="작업완료")

def task():
    threading.Thread(target=long_task).start()

app = tk.Tk()
label = tk.Label(app, text='작업중......')
label.pack()

btn = tk.Button(app, text="시작", command=task)
btn.pack()

app.mainloop()