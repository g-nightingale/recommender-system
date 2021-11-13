class config:
    """Config class."""

    ratings_data = "data/ratings.csv"
    movies_data = "data/movies.csv"
    ratings_features_to_drop = ['timestamp']
    movies_features_to_drop = ['genres']
    sample_n = 20000
    random_state = 42
    movies_to_keep_n = 100
