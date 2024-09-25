# 주석 ctrl + /
# 주석은 코드 실행에 영향을 주지 않습니다.
print('hi') #콘솔 프린트
'''
다중 주석
코드에 영향을 주지 않습니다.
'''
#정수형에 실수를 넣어도 자동으로 타입을 받아들이기 때문에 오류가 나지 않습니다.
# import를 사용해 설치한 라이브러리를 가져다 씁니다.

num = 10    #python은 타입 선언을 하지 않습니다.
print(num,type(num))
# type() <- 내장함수 변수의 타입을 리턴합니다.
num = 3.14; #다른 타입을 할당해도 오류가 나지 않습니다.
print(num,type(num))
# 변수는 예약어 사용이 안되며 스네이크 표기법을 사용합니다.
mem_nm = "Hello, 1BIN"
msg = '''
    문자열이 길 때 """ 작은 따옴표 or 큰 따옴표 3개로 열고 닫습니다.
'''
print(msg)
print('Hello' * 100)    #문자열 곱하기 가능
nm = mem_nm.replace('Hello', 'hi')
print(nm)
arr = nm.split(',') # 구분자로 잘라서 배열로 리턴합니다.(default:공백 1)
print(arr)

# 동적배열(Dynamic Array)
# [] <--비어있는 배열
arr2 = [1, True, "Hi", [2, 3, ['1BIN']]]    #배열 요소 type이 자유롭습니다.
print(arr2[1])          #index 1번 value에 접근
print(arr2[3][2])       #index 3번의 2번 째 요소
print(arr2[3][2][0])    #index 3번의 2번 째의 0번 째 요소
print(arr2[-1])         #마지막 요소
arr3 = [1,2,3,4,5] * 10 #배열 곱하기 가능
print(arr3)

#slice 가능
print(arr3[1:4])    # 1 인덱스부터 4인덱스 -1까지
print(arr3[ :3])    # 처음부터 3인덱스 -1까지
print(arr3[3: ])    # 3인덱스부터 끝까지
print(len(arr3))    #len: 배열 사이즈를 리턴

#튜플(tuple): 배열과 달리 수정이 불가능합니다. 인덱스로 데이터에 접근합니다. 슬라이싱을 지원합니다.
t = (1,2,3)     #수정이 안되기 때문에 초기값 할당이 필요합니다.
print(t[-1])
print(t[0])
print(t[1: ])
t2 = (7,8)
t3 = t + t2     #병합은 됩니다. 기존 것에 재할당아 아니라, 합쳐서 새로운 튜플을 만드는 것이기 때문에 됩니다.
print(t3)
#t3[1] = 1 << 이런식으로 수정하려고 하면 오류가 발생합니다.

#dictionary (dict): key-value 쌍을 요소로 가지는 자료형입니다.
# {} 비어있는 딕셔너리
mate = {"팽수":100, "길동":90, '동길':80}
print(mate, type(mate))
print(mate['팽수'])   #key로 value접근
mate['팽수'] = 99     #수정
print(mate.items())
print(mate.keys())
print(mate.values())

# set: 중복을 허용하지 않습니다.
# set() <--비어있는 set 선언
lotto = {1,2,2,3,4,5} #중괄호지만, 키밸류가 아니기 때문에 set입니다.
print(lotto, type(lotto))   #set은 중복을 허용하지 않기 때문에, 1,2,3,4,5만 출력됩니다.
my_set = {} # 이건 딕셔너리
print(my_set, type(my_set))
my_set = set()  #이건 set
print(my_set, type(my_set))
