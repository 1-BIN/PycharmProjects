import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df_ratings = pd.read_csv("ratings.csv")
df_movies = pd.read_csv("movies.csv")

df_ratings.drop('timestamp', axis=1, inplace=True)  #날짜는 필요없어서 버립니다.
user_item_rating = pd.merge(df_ratings, df_movies, on='movieId')
print(user_item_rating.head(10))
movie_matrix = user_item_rating.pivot_table('rating', index='title', columns='userId')
print(movie_matrix)
movie_matrix.fillna(0, inplace=True)#유저평점이 없는 nan을 0으로 바꿉니다.
item_cf = cosine_similarity(movie_matrix)
result_df = pd.DataFrame(data=item_cf, index=movie_matrix.index, columns=movie_matrix.index)
print(result_df)
def get_item_based(title):
    return result_df[title].sort_values(ascending=False)[:10]
while True:
    movie = input("좋아하는 영화 이름을 정확하게! 입력하세요: ")
    print(get_item_based(movie))