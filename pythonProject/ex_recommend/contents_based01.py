import numpy as np
import pandas as pd

def cos_sim(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))


def fn_sim(user, items):
    sim_arr=[]
    for item in items:
        sim_arr.append(round(cos_sim(user, item), 3))
    return sim_arr

df = pd.read_excel('./item_metric.xlsx')
#고객 프로파일링 데이터
user_metric = [1, 0, 0.33, 0.67, 0.67, 0.67, 0.33, 0, 0.67, 0.33]
item_arr = []
for i in range(len(df.index)):
    item_arr.append(df.loc[i].tolist())
print(fn_sim(user_metric, item_arr))