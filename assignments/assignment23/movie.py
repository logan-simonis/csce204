class Movie:
    def __init__(self, title, description, actors, genre, rating):
        self.title = title
        self.description = description
        self.actors = actors
        self.genre = genre
        self.rating = rating
        
    def display(self):
        print(f"""
        *** {self.title} ***
        {self.description}
        Stars: 
        - {self.actors[0]}
        - {self.actors[1]}
        - {self.actors[2]}
        Genre: {self.genre}
        Rating: {self.rating} stars
        """)
    
    def is_match(self, title):
        if title == self.title:
            return True
        else:
            return False