import numpy as np
import pandas as pd

def sample_data_and_transform(df, sample_n, movies_to_keep_n=None) -> pd.DataFrame:
    """Sample and transform the ratings data."""
    sample = df.head(sample_n)
    sample = sample.pivot(index='userId', 
                          columns='movieId', 
                          values='rating')

    if movies_to_keep_n is not None:
        movies_to_keep = sample.count(axis=0).sort_values(ascending=False).index[:movies_to_keep_n]
        sample = sample[movies_to_keep]

    return sample

def create_movies_dictionary(df):
    """Create movies dictionary."""
    movies_dictionary = {}
    ids = [i for i in df['movieId'].values]
    titles = [i for i in df['title'].values]

    for i, id in enumerate(ids):
        movies_dictionary[id] = titles[i]

    return movies_dictionary

def create_item_dictionary(item_list):
    """Create item dictionary."""
    item_dictionary = {}
    for i, item in enumerate(item_list):
        item_dictionary[i] = item
    return item_dictionary

def cosine_similarity(arr1, arr2):
    """Calculates the cosine similarity between two arrays."""
    return np.dot(arr1, arr2) / (np.sqrt(np.sum(arr1 ** 2)) * np.sqrt(np.sum(arr2 ** 2)))

def create_similarity_vector(df, method=None):
    """Create the item similarity vector."""

    # Convert Pandas DataFrame to numpy to speed things up
    matrix = df.to_numpy()

    # Create an empty matrix to store the item similarities
    sim_vector = np.zeros(int(df.shape[1] * (df.shape[1] + 1)/2.0))

    # Populate the similarity vector
    c = 0
    for i in range(df.shape[1]):
        for j in range(i, df.shape[1]):
            # Identify rows with no np.nan
            z = ~np.isnan(matrix[:, [i, j]]).any(axis=1)
            sim_vector[c] = cosine_similarity(matrix[z, i], matrix[z, j])
            c += 1

    return sim_vector

def retrieve_similarity(item_1, item_2, sim_vector, n_categories):
    """Return item similarities from the similarity ctor."""
    i = min(item_1, item_2)
    j = max(item_1, item_2)
    return sim_vector[int(i*(n_categories-1) + j - (i-1)*(i)/2.0)]

def calculate_predicted_rating(item, user_ratings_vector, similarity_vector, n_categories):
    """Calculate predicted ratings."""
    # Find all the items that the user has rated
    items_with_ratings = [i[0] for i in enumerate(~np.isnan(user_ratings_vector).values) if i[1]]
    weighted_ratings = []
    sim_sum = 0

    # Calculate predicted ratings
    for i in items_with_ratings:
        sim = retrieve_similarity(item, i, similarity_vector, n_categories)
        sim_sum += sim
        weighted_ratings.append((sim * user_ratings_vector[i]))
    return sum(weighted_ratings)/sim_sum

def create_recommendations(user_ratings_vector, similarity_vector):
    """Create recommendations for a user."""
    
    # Get the number of categories
    n_categories = len(user_ratings_vector)

    # Find all the items a user hasn't rated
    items_without_ratings = [i[0] for i in enumerate(np.isnan(user_ratings_vector).values) if i[1]]

    predicted_ratings = []
    for i in items_without_ratings:
        pred_rating = calculate_predicted_rating(i, user_ratings_vector, similarity_vector, n_categories)
        predicted_ratings.append((i, pred_rating))

    # Sort the ratings
    predicted_ratings = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)

    return predicted_ratings

def decode_recommendations(recommendations, dictionary, movie_dictionary, top_n=10):
    """Decode recommendations."""
    for i in range(top_n):
        movie_id = dictionary[recommendations[i][0]]
        rating = round(recommendations[i][1], 4)
        print(f"movie: {movie_dictionary[movie_id]} pred rating: {rating}")
