class Song:
    count = 0
    genre_count = []
    artist_count = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1  # Increases the count when a new song is added.
        self.add_to_genres()
        self.add_to_artists()

    def add_to_genres(self):
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 0
        Song.genre_count[self.genre] += 1

    def add_to_artists(self):
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 0
        Song.artist_count[self.artist] += 1

    @classmethod
    def get_genres(cls):
        # Returns list of all the keys(genres) from the `genre_count` dict of the `Song` class.
        return list(cls.genre_count.keys()) # => Accesses the `genre_count` dict of the `Song` class.
                                            # => Retrieves all the keys(genres) from this dict.
                                            #  => Converts the keys to a list format.
            # `.keys()` => Dict method that returns a view object of all keys in the `genre_count` dict of the `Song` class.
            #  `list` => Creates a list object.
    

    @classmethod
    def get_artists(cls):
        return list(cls.artist_count.keys())# => Accesses the `artist_count` dict of the `Song` class.
                                            # => Retrieves all the keys(artists) from this dict.
                                            #  => Converts the keys to a list format.