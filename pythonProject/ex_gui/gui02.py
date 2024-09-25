from tkinter import *
# pip install pillow    이미지 리사이징, 변경 등을 도와주는 라이브러리입니다.
from PIL import Image, ImageTk
def move_left(event):
    print('왼쪽')
    canvas.move(item, -20, 0)
def move_right(event):
    print('오른쪽')
    canvas.move(item, 20, 0)
def move_up(event):
    print('위')
    canvas.move(item, 0, -20)
def move_down(event):
    print('아래')
    canvas.move(item, 0, 20)

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack()          # ↓ x1, y1, x2, y2 사각형에 내접하는 원을 그림. (사각형의 좌상단과 우하단 좌표)
item = canvas.create_oval(100, 150, 150, 200, fill='yellow')    #create.oval이 동그라미를 그려줍니다.
app.bind('<Left>', move_left)
app.bind('<Right>', move_right)
app.bind('<Up>', move_up)
app.bind('<Down>', move_down)
app.mainloop()
