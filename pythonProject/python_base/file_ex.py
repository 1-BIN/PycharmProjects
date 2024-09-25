import os
#root = "C:\\"
# 파일 시스템의 디렉토리 트리를 반복적으로 순회
# 주어진 경로의 하위 디렉토리와 파일을 재귀적으로 탐색
# root: 현재 디렉토리 경로, dirs: 하위 디렉토리 목록, files: 해당 디렉토리 내의 파일 목록
#for root, dirs, files in os.walk(root):
#    print(root, dirs, files)

# 시작 경로, 찾을 파일명을 입력받아
# 찾으면 '찾았습니다.' & 파일 천제 경로 출력.

def fn_find():
    input1 = input("찾을 '시작경로 파일명'을 입력하세요").split(' ')
    root = input1[0]
    name = input1[1]
    for root, dirs, files in os.walk(root):
        for file in files:
            if file == name:
                print(file)
                input2 = input("이 파일이 맞나요? (y/n)")
                if input2 == 'y':
                     print(os.path.join(root, file))
                elif input2 =='n':
                     print('까비..')
                return
fn_find()
##C:// file.py