class Book:
    def __init__(self,title=None,author=None,genre=None):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"{} {} {}"