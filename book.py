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

    def toArray(self):
        return [{"id": self.id,
        "name": self.name,
        "type": self.book_type,
        "genres": self.genres,
        "authors": self.authors,
        "year": self.year}]

    def writeToFile(self, path):
        with open(path, 'w') as file:
            file.write(json.dumps(self.toArray(), sort_keys=True, indent=4))

    def updateFromJson(self, data):
        dct = json.loads(data)
        print(dct)
        dct = dct[0]
        self.id = dct['id']
        self.name = dct["name"]
        self.book_type = dct["type"]
        self.genres = dct["genres"]
        self.authors = dct["authors"]
        self.year = dct["year"]
