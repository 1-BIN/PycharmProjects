# 함수 선언 def:

def adder(a, b):
    sum = a + b
    return sum

print(adder(10, 2))
# return 0개~ 여러 개 가능합니다.
def return_test():
    return 10, "^^", 3.14
a, b, c = return_test()
print(a, b, c)
data = return_test()
print(data)
# 디폴트 매개 변수
def fn_default(nm, level=1):
    print(nm, level)
fn_default('팽수')
fn_default('길동', 10)
# 가변 매개변수 (0 ~ n개)
def fn_calc(operator, *args):
    result = 0
    if operator == '+':
        for n in args:
            result += n
    elif operator == '*':
        result = 1
        for n in args:
            result *= n
    return result
print(fn_calc('+', 1,2,3,4,5,6,7))
print(fn_calc('+'))
print(fn_calc('*',10,9))