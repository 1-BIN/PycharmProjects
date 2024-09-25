#로또번호 생성
#사용자 입력 수량만큼
# 1 ~ 45의 6자리 로또번호를 생성하여 출력하시오
import random
# 비어있는 set
    #ex = set()
# 요소 추가
    #ex.add(5)
    #print(ex)
# set 길이
    #print(len(ex))

num = int(input("몇 개 만들어드릴깝숑?"))
for i in range (num):
    lotto = set()       #반복할 때마다 배열이 초기화 되어야하기 때문에 반복문에 빈배열 선언을 포함해줍니다.
    while len(lotto) < 6:
        numbers = random.randint(1, 45)
        lotto.add(numbers)
    print("행운의 로또 번호는: ", lotto)