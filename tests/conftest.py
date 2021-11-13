import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def input_two_arrays():
    arr1 = np.array([1, 4, 5, 3, 4, 5])
    arr2 = np.array([2, 3, 4, 1, 3, 3])
    return arr1, arr2

@pytest.fixture
def input_data():
    df = pd.DataFrame({'col1':[np.nan, 1, 3, 4],
                       'col2':[1, 1, 3, 3],
                       'col3':[2, 5, 1, 2]})

    return df

@pytest.fixture
def input_similarity_vector():
    vector = np.array([1.0, 0.9648, 0.5381, 1.0, 0.6136, 1.0])
    return vector