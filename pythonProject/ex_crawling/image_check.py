import os
img_dir = "./돌고래"
count = 0
for filename in os.listdir(img_dir):
    file_path = os.path.join(img_dir, filename)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        #1KB 미만 파일을 지웁니다.
        if file_size < 1024:
            os.remove(file_path)
            count += 1
print(count)