from keras.models import load_model
import pandas as pd
import numpy as np
import joblib

#모델 로드
model = load_model('./AAPL.h5')
#스케일러 로드
scaler = joblib.load('./scaler.save')
#테스트 데이터 로드
df = pd.read_excel('./AAPL_20240805_20241015.xlsx')
df_data = scaler.transform(df['Close'].values.reshape(-1,1))

data_reshape = np.reshape(df_data, (1, 50, 1))
pred = model.predict(data_reshape)
print(pred)

#역변환
pred_inverse = scaler.inverse_transform(pred)
print(f"내일 주가는: {pred_inverse}")