# media.py
# Class defination for movie trailer website
import webbrowser


class Movie():
    """ This class is used to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # Initializing and creating the memory space for instance variable
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Open the movie trailer in the Webpage browser
        webbrowser.open(self.trailer_youtube_url)
