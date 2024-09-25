#반복문 for
arr = ['팽수','길동','동길']
#방법1. 값만 필요할 때
for v in arr:
    print(v)
#방법2. 값, 인덱스 둘다 필요할 때
for i, v in enumerate(arr):
    print(i,v)
#방법3. 단순 횟수 반복
for i in range(3):
    print(i)
for i in range(len(arr)):
    print(arr[i])
for i in range(1, 4):
    print(i)    # 1부터 4 -1 까지
for i in range(2, 11, 2):
    print(i)    # 2부터 11 -1 까지 2씩 증가

#dictionary for문
#원래는 키-값 순서를 보장해주지 않지만, 3.6버전 이후로 키-값 순서를 보장해줌
dic = {"수학":100, "영어":60, "국어":90}
for k in dic:   # k 자리에 오는 것은 key 입니다.
    print(k, dic[k])