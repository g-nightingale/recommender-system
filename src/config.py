class config:
    """Config class."""

    ratings_data = "data/ratings.csv"
    movies_data = "data/movies.csv"
    ratings_to_drop = ['timestamp']
    movies_to_drop = ['genres']
    sample_n = 20000
    random_state = 42
    most_popular_movies_50 = [356, 318, 296, 593, 2571, 50, 110, 527, 260, 592, 
                              47, 1198, 457, 1196, 780, 589, 588, 150, 1, 480, 590, 
                              1210, 364, 32, 2959, 3578, 1580, 2028, 380, 858, 165, 
                              367, 316, 58559, 344, 153, 648, 4993, 2762, 595, 5952, 
                              608, 597, 231, 1704, 1036, 1617, 377, 924, 293]
# config = config_setup()