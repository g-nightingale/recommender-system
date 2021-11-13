class config:
    """Config class."""

    userid = 3
    ratings_data = "data/ratings.csv"
    movies_data = "data/movies.csv"
    ratings_features_to_drop = ['timestamp']
    movies_features_to_drop = ['genres']
    sample_n = 50000
    random_state = 42
    movies_to_keep_n = 20
