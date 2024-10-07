# pip install pillow    이미지 리사이징, 변경 등을 도와주는 라이브러리입니다.
from PIL import Image, ImageTk
from tkinter import *


def move_left(event):
    print('왼쪽')
    canvas.move('tiger', -20, 0)
def move_right(event):
    print('오른쪽')
    canvas.move('tiger', 20, 0)
def move_up(event):
    print('위')
    canvas.move('tiger', 0, -20)
def move_down(event):
    print('아래')
    canvas.move('tiger', 0, 20)

def jump(event):
    jump_height = 10
    canvas.update()
    canvas.after(20)
    #Move the ball upwards
    for _ in range(jump_height):
        canvas.move('tiger', 0, -20)
        canvas.update()
        canvas.after(20)
    #Make the ball fall down

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack()          # ↓ x1, y1, x2, y2 사각형에 내접하는 원을 그림. (사각형의 좌상단과 우하단 좌표)
img = Image.open('tiger.png')
img = img.resize((100,100))
item = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image=item, tag='tiger')  #함수에서 태그로 사용합니다.
#item = canvas.create_oval(100, 150, 150, 200, fill='yellow')    #create.oval이 동그라미를 그려줍니다.
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.bind('<space>',jump)
canvas.focus_set()

app.mainloop()
