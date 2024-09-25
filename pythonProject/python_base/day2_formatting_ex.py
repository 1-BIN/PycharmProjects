# 함수를 작성하세요!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# input :원가, 할인율
# output:할인 금액,계산 금액
# fn_sales_price

def fn_sales_price(pri, disc):
    a = pri * (disc/100)    #깎아 준 금액
    b = pri - a
    print(f"할인퍼센트 : {disc}%")
    print(f"원가 : {pri}원")
    print(f"할인 금액 : {a:.2f}원")  #소수점 둘째 자리까지 출력
    print(f"계산할 금액 : {b}원")
print(fn_sales_price(10000,20))

