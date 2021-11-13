import os, sys
sys.path.insert(1, os.getcwd())
from src.util import create_similarity_vector, retrieve_similarity


def test_retrieve_similarity(input_data):
    """Test create_similarity_matrix function."""

    # Given
    similarity_vector = create_similarity_vector(input_data)

    # When
    n_categories = input_data.shape[1]

    sim_1 = retrieve_similarity(0, 0, similarity_vector, n_categories)
    sim_2 = retrieve_similarity(0, 1, similarity_vector, n_categories)
    sim_3 = retrieve_similarity(1, 0, similarity_vector, n_categories)
    sim_4 = retrieve_similarity(1, 2, similarity_vector, n_categories)
    sim_5 = retrieve_similarity(2, 1, similarity_vector, n_categories)
    sim_6 = retrieve_similarity(2, 2, similarity_vector, n_categories)

    # Then
    assert round(sim_1, 1) == 1.0
    assert round(sim_2, 4) == 0.9898
    assert round(sim_3, 4) == 0.9898
    assert round(sim_4, 4) == 0.6136
    assert round(sim_5, 4) == 0.6136
    assert round(sim_6, 1) == 1.0
