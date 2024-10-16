import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df_ratings = pd.read_csv('ratings.csv')
df_movies = pd.read_csv('movies.csv')
df_ratings.drop('timestamp', axis=1, inplace=True)

user_item_rating = pd.merge(df_ratings, df_movies, on='movieId')
user_matrix = user_item_rating.pivot_table('rating', index='userId', columns='title')
user_matrix.fillna(0, inplace=True)
user_cf = cosine_similarity(user_matrix)
result_df = pd.DataFrame(data=user_cf, index=user_matrix.index, columns=user_matrix.index)

# 대상 유저와 유사한 유저의 평점 놓은 영화(본 영화 제외)
def get_user(id, orderId):
    movie_arr = user_item_rating[user_item_rating['userId'] == id]
    user_watch_movie = user_item_rating[user_item_rating['userId'] == orderId]
    # ~ : 제외 의미
    movie_arr = movie_arr[~movie_arr['movieId'].isin(user_watch_movie['movieId'].values.tolist())]
    five_movie = movie_arr.sort_values(by='rating', ascending=False)[:6]
    return five_movie['title'].values.tolist()
# 대상 유저와 유사한 유저를 찾고 영화 리스트 생성
def get_user_item(id):
    my_best = user_item_rating[user_item_rating['userId'] == id].sort_values(by='rating', ascending=False)[:5]
    print("my_best")
    print(my_best['title'])
    #유사도 점수 높은 유저
    sim_user = result_df[id].sort_values(ascending=False)[:6]
    sim_id = sim_user.index.tolist()[1:]
    data=[]
    for i in sim_id:
        print("sim user id: " + str(i))
        item = get_user(i, id)
        data = data + item
    return set(data) #중복 영화 제외
while True:
    user_id = input("target user id: ")
    recommend_movie = get_user_item(int(user_id))
    print(recommend_movie)