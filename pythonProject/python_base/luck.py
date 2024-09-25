import random
# 함수명: make_lotto
# input: 없음
# ouput: 로또번호

#매개변수 사용하기
# def make_lotto(num):
#     for i in range(num):
#         lotto = set()
#         while len(lotto) < 6:
#             numbers = random.randint(1, 45)
#             lotto.add(numbers)
#         print("행운의 로또 번호는: ", lotto)


#매개 변수 없이 만들기
# def make_lotto2():
#         lotto = set()
#         while len(lotto) < 6:
#             numbers = random.randint(1, 45)
#             lotto.add(numbers)
#         return lotto
# print(make_lotto2())


def make_lotto3():
    lotto = set()
    while len(lotto) < 6:
        numbers = random.randint(1, 45)
        lotto.add(numbers)
    return sorted(list(lotto))
#print(make_lotto3())

#list.sort()    <-리스트 자체를 정렬
#sorted(list)   <-정렬된 새로운 리스트를 리턴
#arr = make_lotto()
#arr.sort    #기본 오름차순 정렬
#arr.sort(reverse=True) #내림차순 정렬
#print(arr)

#함수명    :user_lotto
#input    :0~n
#output   :로또번호, 'x x 번호가 적용된 로또 번호' <--메시지 리턴
#사용자가 입력한 번호를 포함시켜서 로또번호 생성
#단, 6개 이상이 들어오면 5개까지만 포함하고 나머지 1개는 랜덤값




if __name__ == '__main__':      # main을 입력하면 자동완성이 뜹니다. 파일 자체 실행 때만 실행 되게 합니다.
    def user_lotto(*args):
        user_num = list(args)[:5]
        print(user_num)
        m = ','.join(map(str, user_num)) + ' 번호가 적용된 로또'  # 리스트 user_num을 ','을 삽입하여
        # 문자열로 만들어 결합했습니다.
        lotto = set(user_num)  # user_num이 포함된 set이 만들어집니다.와우.
        while len(lotto) < 6:
            numbers = random.randint(1, 45)
            lotto.add(numbers)
        return m, sorted(list(lotto))


    print(user_lotto(1, 2, 3))
    arr = [1,2,3]
    message = ','.join(map(str,arr))    #map(function,iterable)
    print(message)
else:   #다른 모듈에서 실행했을 경우
    print("임포트 하셨군요")