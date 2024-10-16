import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify
from flask_cors import CORS

#샘플 고객 데이터
data = { 'mem_id':[1,2,3,4,5]
        ,'mem_nm':['우디','닉','주디','티몬','심바']
        ,'leisure':[3, 5, 2, 4, 1]
        ,'social_media':[4, 3, 5, 2, 1]
        ,'music_genre':[2, 4, 1, 5, 3]
        ,'food_preference':[5, 1, 4, 3, 2]
        ,'travel_style':[1, 3, 5, 2, 4]
}
customer_df = pd.DataFrame(data)
# 고객 유사도 계산 함수
def get_similar(input_form, df):
    #새로운 고객 데이터를 df에 추가                 #두번째 열 ~ 마지막 열의 이름
    new_customer = pd.DataFrame([input_form], columns=df.columns[2:])
    temp_df = pd.concat([df, new_customer], ignore_index=True)
    #유사도 계산
    sim_matrix = cosine_similarity(temp_df.iloc[:, 2:])
    #[-1]마지막원소, [:-1]마지막 행에서 마지막 열을 제외한
    new_customer_sim = sim_matrix[-1][:-1]  #새로운 고객과 기존 고객 간 유사도
    print(new_customer_sim)
    #유사도가 높은 고객 상위 3명
    sim_idx = np.argsort(-new_customer_sim)[:3]
    sim_customer = df.iloc[sim_idx]
    return sim_customer

app = Flask(__name__)
CORS(app)   #CORS 오류 났을 때. 전체 허용



@app.route('/get_similar', methods=['POST'])
def get_similar_main():
    global customer_df
    user_data = [
         int(request.form['leisure'])
        ,int(request.form['social_media'])
        ,int(request.form['music_genre'])
        ,int(request.form['food_preference'])
        ,int(request.form['travel_style'])
    ]
    #입력 정보와 유사 고객 찾기
    similar_user = get_similar(user_data, customer_df)

    seq = customer_df['mem_id'].max() + 1
    new_data = {
          'mem_id': seq
        , 'mem_nm': request.form['mem_nm']
        , 'leisure': user_data[0]
        , 'social_media': user_data[1]
        , 'music_genre': user_data[2]
        , 'food_preference': user_data[3]
        , 'travel_style': user_data[4]
    }
    customer_df = pd.concat([customer_df, pd.DataFrame([new_data])], ignore_index=True)
    print(customer_df)

    # 결과 반환
    return jsonify(similar_user.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')