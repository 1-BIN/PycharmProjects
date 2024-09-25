# w rite, a ppend:수정(merge와 비슷), r ead

f = open('diary.txt', 'a', encoding='utf8')
f.write('오늘의 일기...\n')
while True:
    n =input('내용입력:(종료q)')
    if 'q' == n:
        break
    f.write(n)
    f.writelines('\n')
f.close()       #파일은 꼭 열고 닫고를 해줘야합니다. 안 그러면 열려있어요.