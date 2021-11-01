from fastapi import FastAPI
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np



app = FastAPI()

credits = pd.read_csv("tmdb_5000_credits.csv")
movies_df = pd.read_csv("tmdb_5000_movies.csv")
credits_column_renamed=credits.rename(index=str, columns={"movie_id":"id"})
movies_df_merge = movies_df.merge(credits_column_renamed, on='id')
movies_cleaned_df = movies_df_merge.drop(columns=['homepage','title_x','title_y','status','production_countries'])
movies_cleaned_df['overview']=movies_cleaned_df['overview'].fillna('')



tfv =TfidfVectorizer(min_df=3,max_features=None,strip_accents='unicode',analyzer='word',token_pattern='\w{1,}',ngram_range=(1,3),stop_words = 'english')
tfv_matrix = tfv.fit_transform(movies_cleaned_df['overview'])
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

indices=pd.Series(movies_cleaned_df.index, index=movies_cleaned_df['original_title']).drop_duplicates()

@app.get("/")
async def root():
    return {"Title ": "Movie Recomendation API service"}


@app.get("/recommendation/{movie_name}")
async def get_recommendation(movie_name: str):
    
    idx=indices[movie_name]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores= sorted(sig_scores, key=lambda x: x[1],reverse = True)
    sig_scores=sig_scores[1:11]
    movie_indices = [i[0] for i in sig_scores]
    return movies_cleaned_df['original_title'].iloc[movie_indices].to_dict()


    
