# 반복문 while <조건식>: True일 경우 반복합니다.
i = 1
while i <= 5:
    i += 1           # python에는 증감 연산자(++, --)가 없습니다.
    if i == 2:
        #continue    # continue를 만나면 하위 내용을 건너뜁니다.
        break   #만나면 반복문 즉시 종료
    print(i)

flag = True     #(True, False 첫 대문자 유의)
while flag:
    msg = input("종료(q)")
    if msg == 'q':
        flag = False
