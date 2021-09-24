import json

class Book:
    current_id = 0
    all_ids = []

    def __init__(self, name, book_type, genres, authors, year):
        while self.current_id in self.all_ids:
            self.current_id += 1
        self.id = self.current_id
        self.name = name
        self.book_type = book_type
        self.genres = genres
        self.authors = authors
        self.year = year
        self.all_ids.append

    def __init__(self, data):
        if data["id"] in self.all_ids:
            msg = "Cannot create book: Id already taken."
            print(msg)
        else:
            Book.readFromJson(self, data)

    def toArray(self):
        return {"id": self.id,
        "name": self.name,
        "type": self.book_type,
        "genres": self.genres,
        "authors": self.authors,
        "year": self.year}

    def writeToFile(self, path, addComma):
        with open(path, 'a') as file:
            if addComma:
                file.write("\n\t,")
            file.write(json.dumps(self.toArray(), sort_keys=True, indent=8))

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
    
    def toString(self):
        result = ""
        result += "id: " + str(self.id) + "\n"
        result += "name: " + self.name + "\n"
        result += "type: " + self.book_type + "\n"
        result += "genres: " + str(self.genres) + "\n"
        result += "authors: " + str(self.authors) + "\n"
        result += "year: " + str(self.year) + "\n"
        return result
