import os, sys
sys.path.insert(1, os.getcwd())
from src.util import create_similarity_vector, calculate_predicted_rating


def test_calculate_predicted_rating(input_data):
    """Test calculate_predicted_rating function."""

    # Given
    similarity_vector = create_similarity_vector(input_data)

    # When
    n_categories = input_data.shape[1]
    user_ratings_vector = input_data.iloc[0, :]
    pred_rating = calculate_predicted_rating(0, user_ratings_vector, similarity_vector, n_categories)

    # Then
    assert round(pred_rating, 4) == 1.3666
