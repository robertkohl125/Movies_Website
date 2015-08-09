import media
import fresh_tomatoes
"""This file holds the movie and tv show information"""
# Movies to be displayed are listed here.  
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://bit.ly/1IBuCvo", # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "http://imdb.to/1NjiB11")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://bit.ly/1J46ask", # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1")
star_wars_the_force_awakens = media.Movie("Star Wars The Force Awakens",
                                          "There's been an awakening.",
                                          "http://bit.ly/1hrvQ5N",
                                          "https://www.youtube.com/watch?v=OMOVFvcNfvE",
                                          "http://www.imdb.com/title/tt2488496/?ref_=fn_al_tt_1")
the_wild_bunch = media.Movie("The Wild Bunch",
                             "They came too late and stayed too long.",
                             "http://bit.ly/1gUs9Wu", # noqa
                             "https://www.youtube.com/watch?v=aIwH96iZI7E",
                             "http://www.imdb.com/title/tt0065214/?ref_=fn_al_tt_1")
mad_max_fury_road = media.Movie("Mad Max - Fury Road",
                                "What a lovely day.",
                                "http://bit.ly/1MdVjeq", # noqa
                                "https://www.youtube.com/watch?v=hEJnMQG9ev8",
                                "http://www.imdb.com/title/tt1392190/?ref_=fn_al_tt_1")
jurassic_world = media.Movie("Jurassic World",
                             "The park is open.",
                             "http://bit.ly/1IBBQ2H", # noqa
                             "https://www.youtube.com/watch?v=RFinNxS5KN4",
                             "http://www.imdb.com/title/tt0369610/?ref_=fn_al_tt_1")

movies = (toy_story,avatar,star_wars_the_force_awakens,the_wild_bunch,mad_max_fury_road,jurassic_world)
fresh_tomatoes.open_movies_page(movies)



