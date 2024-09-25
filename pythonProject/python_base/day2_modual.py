import math
# math 모듈 안에 있는 factorial 함수 호출
print(math.factorial(5))
from math import factorial as f
# math 모듈 안에 있는 factorial 함수를 f로 별칭을 붙여 호출
print(f(10))
import luck     #동일한 경로에 있기 때문에 이렇게 쓸 수 있고, 다른 폴더에 있는 경우 폴더까지 표시해줍니다.
# print(luck.make_lotto2())   # luck 안에 많은 함수가 있어 많이 호출되니, 그 중에 선택해줘야합니다.
