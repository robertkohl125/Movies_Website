import webbrowser


class Video():
    """This Parent class constructs a list of media variables for the
    child classes Video and TvShow for our web site."""
    # This is the Parent class for the media classes (Movie and TvShow).
    def __init__(self, title, storyline, poster_image_url, 
                 trailer_youtube_url, open_imdb_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.open_imdb_url = open_imdb_url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
class Movie(Video):
    """This file keeps a list of movie info for the web site."""
    # This is the Child class from Parent class Video() that holds movie info.
    def __init__(self, title, storyline, poster_image_url, 
                 trailer_youtube_url, open_imdb_url):
        Video.__init__(self, title, storyline, poster_image_url, 
                       trailer_youtube_url, open_imdb_url)
