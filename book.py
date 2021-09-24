import json

class Book:
    current_id = 0

    def __init__(self, name, book_type, genres, authors, year):
        self.id = self.current_id
        self.current_id += 1
        self.name = name
        self.book_type = book_type
        self.genres = genres
        self.authors = authors
        self.year = year
        allbooks.append(self)

    def __init__(self, data):
        Book.readFromJson(self, data)
        allbooks.append(self)

    def toArray(self):
        return [{"id": self.id,
        "name": self.name,
        "type": self.book_type,
        "genres": self.genres,
        "authors": self.authors,
        "year": self.year}]

    def writeToFile(self, path):
        with open(path, 'a') as file:
            file.write(json.dumps(self.toArray(), sort_keys=True, indent=4))

    def updateFromJson(self, data):
        dct = json.loads(data)
        for book in dct:
            if book['id'] == self.id:
                self.readFromJson(self, book)
                return

    def readFromJson(self, book_data):
        self.id = book_data['id']
        self.name = book_data["name"]
        self.book_type = book_data["type"]
        self.genres = book_data["genres"]
        self.authors = book_data["authors"]
        self.year = book_data["year"]

allbooks = []

def readAllBooks(path):
    with open(path, 'r') as file:
        Book(file.read())