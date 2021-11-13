import os, sys
sys.path.insert(1, os.getcwd())
from src.util import create_similarity_vector


def test_create_similarity_vector(input_data):
    """Test create_similarity_vector function."""

    # Given
    df = input_data

    # When
    sv = create_similarity_vector(df)

    # Then
    assert round(sv[0], 1) == 1.0
    assert round(sv[1], 4) == 0.9898
    assert round(sv[2], 4) == 0.5729
    assert round(sv[5], 1) == 1.0
