
#Movie class that accepts the title, plot, a poster url,
# trailer url, and an optinal rating
class Movie ():
    def __init__ (self, movie_title, movie_storyline, poster_image,
                  trailer_link, movie_rating = "Not yet rated"):
        self.title = movie_title
        self.story = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link
        self.rating = str(movie_rating)
