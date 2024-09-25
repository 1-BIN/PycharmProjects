import random
# random: 난수 생성 관련 기능을 제공합니다.
# 업다운 게임, 세 번의 기회
# 사용자 입력이 맞으면 '정답', 작으면 '업', 크면 '다운' 출력
# 틀릴 때마다 몇 번의 기회가 남았는지 출력

# 파이썬 파일은 하나의 모듈이기 때문에 묘이 파일 이름을 터미널에 입력해도, 업다운 게임이 실행됩니다.

print(('*' * 10) + "업다운 게임" + ('*' * 10))
com_num = random.randint(1, 10)     # 1 ~ 10 정수 리턴
print(com_num)
count = 3

while count > 0:
    num = int(input("1에서 10 사이의 정수를 입력하세요: "))
    if num > com_num:
        print("다운!")
    elif num < com_num:
        print("업!")
    elif num == com_num:
        print("정답입니다!")
        break
    count -= 1
    if count != 0:
        print("남은 기회: ", count)
    else:
        print("다음 기회에... 정답은", com_num)