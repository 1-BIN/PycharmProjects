from tkinter import *
from tkinter import filedialog, messagebox
def new_file():
    print("파일생성")
    text_area.delete(1.0,END)
    app.title("새 파일 - 텍스트 에디터")
def open_file():
    print("파일열기")
    file_path = filedialog.askopenfilename(defaultextension='.txt'  #파일 경로를 가져옵니다.
                                            ,filetypes=[('Text Files', '*.txt'),('All Files','*.*')])
    print(file_path)
    if file_path:
        try:        #다른 형식의 파일을 열 때 오류가 나면
            with open(file_path, 'r', encoding='utf8') as file:      #with는 텍스트나 파일 같은거 알아서 닫아주는 역할입니다.
                content = file.read()
                text_area.delete(1.0, END)
                text_area.insert(END, content)
            app.title(f"{file_path} - 텍스트 에디터")
        except Exception as e:
            print(str(e))   #오류 메시지가 출력되도록 합니다.
            messagebox.showerror('오류',f'파일을 열 수 없습니다.:{e}')
def save_file():
    print("파일저장")
    file_path = filedialog.asksaveasfilename(defaultextension='.txt'  #파일 경로를 가져옵니다.
                                            ,filetypes=[('Text Files', '*.txt'),('All Files','*.*')])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf8') as file:
                content = text_area.get(1.0,END)
                file.write(content)
            app.title(f'{file_path} - 텍스트 에디터')
        except Exception as e:
            messagebox.showerror("오류", f"파일을 저장할 수 없습니다.:{e}")
app = Tk()
app.title("텍스트 에디터")
app.geometry("600x400")

text_area = Text(app)
text_area.pack(fill=BOTH, expand=1)
# 메뉴바 생성
menu = Menu(app)    #큰 메뉴
# 메뉴 생성
file_menu = Menu(menu)  #menu 하위로, file_menu가 들어가게 됩니다.
file_menu.add_command(label='파일 만들기 (작성하기)', command=new_file)
file_menu.add_command(label='파일 가져오기(출력하기)', command=open_file)
file_menu.add_command(label='파일 저장하기', command=save_file)
file_menu.add_separator() # 구분선
file_menu.add_command(label='종료', command=app.quit)
menu.add_cascade(label='파일', menu=file_menu)
app.config(menu=menu)
app.mainloop()