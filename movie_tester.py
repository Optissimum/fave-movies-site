import media
import fresh_tomatoes

#Initial creation of movie list
movie_list = []

momento = media.Movie("Momento",
                "A man with short term memory loss tries to solve the murder of"
                      "his wife.",
                "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg", # NOQA
                "https://www.youtube.com/watch?v=0vS0E9bBSL0")

movie_list.append(momento)

samsara = media.Movie("Samsara",
                      "Exploring the wonders of our world from the mundane to t"
                      "he miraculous.",
                      "https://upload.wikimedia.org/wikipedia/en/7/78/Samsara_Film_Poster.jpg", # NOQA
                      "https://www.youtube.com/watch?v=P0xVp3N-M84",
                      10)

movie_list.append(samsara)

black_dynamite = media.Movie("Black Dynamite",
                             "CIA Agent Black Dynamite must avenge his brother'"
                             "s death while cleaning the streets of a drug that"
                             "is ravaging the community.",
                             "https://upload.wikimedia.org/wikipedia/en/8/84/Black_dynamite_poster.jpg", # NOQA
                             "https://www.youtube.com/watch?v=96Y24a0cyCE",
                             9.5)

movie_list.append(black_dynamite)

speedracer = media.Movie("Speedracer",
                         "Speed Racer an 18-year-old automobile racer who follo"
                         "ws his deceased brother's career as a driver.",
                         "https://upload.wikimedia.org/wikipedia/en/8/82/Speed_racer_ver5_xlg.jpg", # NOQA
                         "https://www.youtube.com/watch?v=8V8sLlqJB2w",
                         9.5)

movie_list.append(speedracer)

fellowship = media.Movie("Lord of the Rings: Fellowship of the Ring",
                         "A hobbit is sent on a journey to stop a reign of dark"
                         "ness as it begins to spread",
                         "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
                         "https://www.youtube.com/watch?v=Pki6jbSbXIY")

movie_list.append(fellowship)

shaolin_soccer = media.Movie("Shaolin Soccer",
                             "A former Shaolin monk reunites his five brothers "
                             "to apply their superhuman martial arts skills to "
                             "play soccer",
                             "https://upload.wikimedia.org/wikipedia/en/3/3e/ShaolinSoccerFilmPoster.jpg",
                             "https://www.youtube.com/watch?v=6FAaOwNnHTA",
                             9.75)

movie_list.append(shaolin_soccer)

fresh_tomatoes.open_movies_page(movie_list)

