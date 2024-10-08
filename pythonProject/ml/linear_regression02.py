import numpy as np
import matplotlib.pyplot as plt

# 공부한 시간 x1, 과외시간 x2 , 성적 y
x1 = np.array([2, 4, 6, 8])
x2 = np.array([0, 4, 2, 3])
y = np.array([81, 93, 91, 97])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, y)
plt.show()

# 기울기 a1, a2, y절편 b
a1 = 0
a2 = 0
b = 0
# 학습률
lr = 0.01
#몇 번 반복할 지 (epochs 에포크)
epochs = 2001
# x 값이 총 몇 개?
n = len(x1)
for i in range(epochs):
    y_pred = a1 * x1 + a2 * x2 + b  # 예측을 구하는 식
    error = y - y_pred  # 실제 값과 비교한 오차
    a1_diff = (2 / n) * sum(-x1 * (error))    #오차를 구하는 함수를 a1로 편미분
    a2_diff = (2 / n) * sum(-x2 * (error))    #오차를 구하는 함수를 a2로 편미분
    b_diff = (2 / n) * sum(-(error))        #오차를 구하는 함수를 b로 편미분
    # 편미분이란 ? 여러 변수에 의해 정의된 함수에서 하나의 변수에 대해 미분하는 것입니다.
    # 나머지 변수는 고정시키고, 특정 변수 하나에 대해서만 함수가 어떻게 변화하는지 알아보는 것.
    # 이 함수가 하나의 변수 x에 대해 어떻게 변화하는지..
    a1 = a1 - lr * a1_diff #학습률을 곱해 기존의 a1 값을 업데이트
    a2 = a2 - lr * a2_diff #학습률을 곱해 기존의 a2 값을 업데이트
    b = b - lr * b_diff #학습률을 곱해 기존의 b 값을 업데이트
    if i % 100 == 0:
        print(f"epochs = {i}, 기울기 a1 = {a1}, 기울기 a2 = {a2}, y 절편 = {b}")