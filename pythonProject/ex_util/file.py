import os
# os는 python 표준 라이브러리로 운영체제와 상호작용하는 다양한 기능을 제공합니다. (파일 탐색, 삭제, 변경 ...)
folder = os.getcwd() #현재 위치
print(folder)
# 폴더,파일 리스트
file_list = os.listdir(folder)
for f in file_list:
    file_path = os.path.join(folder, f) #경로 결합
    if os.path.isfile(file_path):   #isfile, isdir: 파일인지 폴더인지 확인합니다.
        print('파일이구만', file_path)
    if os.path.isdir(file_path):
        print('폴더구만', file_path)

# 파일 삭제 os.remove('경로')
# 비어있는 폴더 삭제 os.rmdir('경로')
import shutil
# 파일있는 폴더 전체삭제
# shutil.rmtree('경로')
#os.remove('C:/dev/PycharmProjects/pythonProject/ex_util/test/test')
#os.rmdir('C:/dev/PycharmProjects/pythonProject/ex_util/test')

#폴더 생성
image_dir = './img'
if not os.path.exists(image_dir):   #해당 경로가 존재하지 않으면
    os.makedirs(image_dir)
