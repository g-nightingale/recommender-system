import pandas as pd
import numpy as np
import os, sys
sys.path.insert(1, os.getcwd())
from src.config import config
from src.util import create_item_dictionary, create_similarity_vector, create_recommendations, decode_recommendations


def sample_data_and_transform(df, sample_n, columns_to_keep=None) -> pd.DataFrame:
    """Sample and transform the ratings data."""
    sample = df.head(sample_n)
    sample = sample.pivot(index='userId', 
                          columns='movieId', 
                          values='rating')

    if columns_to_keep is not None:
        sample = sample[columns_to_keep]

    return sample

def create_movies_dictionary(df):
    """Create movies dictionary."""
    movies_dictionary = {}
    ids = [i for i in df['movieId'].values]
    titles = [i for i in df['title'].values]

    for i, id in enumerate(ids):
        movies_dictionary[id] = titles[i]

    return movies_dictionary

def main() -> None:
    """Main function."""
    # See - https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/itembased.html
    
    ratings = pd.read_csv(config.ratings_data)
    movies = pd.read_csv(config.movies_data)
    ratings.drop(config.ratings_to_drop, axis=1, inplace=True)
    movies.drop(config.movies_to_drop, axis=1, inplace=True)

    movie_dictionary = create_movies_dictionary(movies)

    sample = sample_data_and_transform(ratings, config.sample_n, 
                                       columns_to_keep=config.most_popular_movies_50)


    item_dictionary = create_item_dictionary(sample.columns.tolist())

    sample.columns = [key for key in item_dictionary.keys()]
    sv = create_similarity_vector(sample)
    user_ratings_vector = sample.iloc[1, :]
    recommendations = create_recommendations(user_ratings_vector, sv)

    decode_recommendations(recommendations, item_dictionary, movie_dictionary, top_n=10)


if __name__ == "__main__":
    main()
