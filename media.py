# media.py
# Class defination for movie trailer website
import webbrowser


class Movie():
    """ This class is used to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, storyline, poster_image, trailer):
        # Initializing and creating the memory space for instance variable
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        # Open the movie trailer in the Webpage browser
        webbrowser.open(self.trailer_youtube_url)
