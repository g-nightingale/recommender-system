import pandas as pd
import numpy as np

import os, sys
sys.path.insert(1, os.getcwd())
from src.util import cosine_similarity


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
            z = ~np.isnan(matrix[:, [i, j]]).any(axis=1)
            sim_vector[c] = cosine_similarity(matrix[z, i], matrix[z, j])
            c += 1

    return sim_vector

def retrieve_similarity(item_1, item_2, sim_vector, n_categories):
    """Return item similarities from the similarity ctor."""
    i = min(item_1, item_2)
    j = max(item_1, item_2)
    return sim_vector[int(i*(n_categories-1) + j - (i-1)*(i)/2.0)]

def calculate_predicted_rating(item, user_ratings_vector, similiarity_vector, n_categories):
    """Calculate predicted ratings."""
    items_with_ratings =  [i[0] for i in enumerate(~np.isnan(user_ratings_vector).values) if i[1]]
    weighted_ratings = []
    sim_sum = 0
    for i in items_with_ratings:
        sim = retrieve_similarity(item, i, similiarity_vector, n_categories)
        sim_sum += sim
        weighted_ratings.append((sim * user_ratings_vector[i]))
        print(f"sim: {sim}, rating: {user_ratings_vector[i]}")
    return sum(weighted_ratings)/sim_sum


if __name__ == "__main__":

    input_data = pd.DataFrame({'col1':[np.nan, 1, 3, 4],
                               'col2':[1, 1, 3, 3],
                               'col3':[2, 5, 1, 2]})

    sv = create_similarity_vector(input_data)
    user_ratings_vector = input_data.iloc[0, :]
    rating = calculate_predicted_rating(0, user_ratings_vector, sv, 3)

    print('similarity vector\n', sv)
    print('user ratings vector\n', user_ratings_vector)
    print(rating)