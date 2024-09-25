'''
    try 블록에서 오류가 발생하면
    except 블록에서 처리할 수 있습니다.

    frinally: 오류, 정상 모두 마지막에 실행합니다.
    else: 정상만 실행합니다
'''
print("프로그램 시작")
try:
    print("1")
    ##result = 10 / 0
    a = "팽수"
    print(a[2])
    print("2")
except ZeroDivisionError as e:      ## 'ZeroDivisionError' 해당 오류일 때만 작동합니다.
    print(f"영으로 왜 나눠.. {e}")    ## 'as ~' alias에 오류 이름을 담아줍니다.
except Exception as e:              ## 위 오류 말고 다른 오류가 날 때 작동합니다.
    print(f"예외가 발생 {e}")
else:
    print("난 정상일 때만 일하는딩")   ## 아무 오류 없이 정상일 때 작동합니다.
finally:                            ## 무조건 작동합니다.
    print("finally: 나는 오류가 나도, 정상 처리가 되어도 아랑곳하지 않고 작동한다.")
print("프로그램 종료")                ## '1'출력 후, 오류가 발생하여 except로 이동.
