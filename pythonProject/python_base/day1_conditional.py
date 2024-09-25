#조건문 if는 조건에 따라 코드 블록을 실행하거나 실행 하지 않도록 제어합니다.
#input 함수는 콘솔 입력을 받는 함수입니다.
#int(), str(), float() <--타입 변환하는 함수
#input은 기본 str으로 리턴됩니다.
num = int(input("숫자를 입력하세요: "))
if num > 10:    #콜론으로 구분
    # 들여쓰기 된 부분이, 해당 조건이 true일 때 실행되는 부분입니다.
    print("입력은 10보다 큼")
elif num == 10:
    print("10입니다")
elif num < 10:
    pass    #아무 작업도 하지 않습니다
print("종료")

#None, [], 0은 False로 인식
arr=[]
if arr:
    print("if 조건 True")
else:
    print("False")  #arr가 비어있기 때문에, false로 갑니다.