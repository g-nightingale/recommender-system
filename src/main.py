import pandas as pd
import os, sys
sys.path.insert(1, os.getcwd())
from src.config import config
from src.util import *


def main() -> None:
    """Main function."""
    # See - https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/itembased.html
    
    # Load in data
    ratings = pd.read_csv(config.ratings_data)
    movies = pd.read_csv(config.movies_data)
    ratings.drop(config.ratings_features_to_drop, axis=1, inplace=True)
    movies.drop(config.movies_features_to_drop, axis=1, inplace=True)
    movie_dictionary = create_movies_dictionary(movies)

    # Create a sample of the data
    sample = sample_data_and_transform(ratings, config.sample_n, 
                                       movies_to_keep_n=config.movies_to_keep_n)

    # Create item dictionary
    item_dictionary = create_item_dictionary(sample.columns.tolist())

    # Rename columns
    sample.columns = [key for key in item_dictionary.keys()]

    # Generate recommendations
    sv = create_similarity_vector(sample)
    user_ratings_vector = sample.iloc[config.userid, :]
    recommendations = create_recommendations(user_ratings_vector, sv)

    # Print recommendations
    decode_recommendations(recommendations, item_dictionary, movie_dictionary, top_n=10)


if __name__ == "__main__":
    main()
