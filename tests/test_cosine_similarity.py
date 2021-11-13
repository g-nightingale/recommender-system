import os, sys
sys.path.insert(1, os.getcwd())
from src.util import cosine_similarity


def test_cosine_similarity(input_two_arrays):
    """Test cosine_similarity function."""

    # Given
    arr1, arr2 = input_two_arrays

    # When
    cs1 = cosine_similarity(arr1, arr2)
    cs2 = cosine_similarity(arr1, arr1)

    # Then
    assert round(cs1, 4) == 0.9631
    assert round(cs2, 1) == 1.0
