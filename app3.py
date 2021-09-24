from flask import Flask, render_template, jsonify, request
import json, os
from book import *
from os.path import exists


app = Flask(__name__)
path = "./data.json"
if not exists(path):
    with open(path, 'w') as file:
        file.write("[]")
books = []


def readBooks():
    global books
    books = []
    with open(path, "r") as file:
        data = file.read()
        jsondata = json.loads(data)
        for b in jsondata:
            books.append(Book(b))
            
readBooks()


@app.route('/api/get/books/', methods=['GET'])
def getBooks():
    string = "" 
    for book in books:
        string += book.toString() + "<br>"
    print(string)
    with open(path, 'r')as file:
        rslt=file.read()
    return rslt
    

@app.route('/api/get/book/<id>', methods=['GET'])
def getBook(id):
    string = "" 
    rslt="["
    for book in books:
        if str(book.id) == id:
            string += book.toString() + "<br>"
            rslt += str(book.toArray()) + "\n"
    print(string)
    rslt+="]"
    return rslt
        
        
        
@app.route('/api/post/book/', methods=['POST'])
def setBook():
    boolean=True
    if len(books) == 0:
        boolean=False
        with open(path, 'w') as file:
            file.write("[]")

    with open(path, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        
    data = json.loads(request.data)
    for i in data:
        book= Book(i)
        if not book:
            book.writeToFile(path, boolean)
         
        
    with open(path, "a") as file:
        file.write("\n]")
   
    readBooks()       
    return "ok"

@app.route('/api/delete/books/', methods=['DELETE'])
def deleteAll():  
    global books
    books = []
    with open(path, 'w') as file:
       file.write("[]")
    return "ok" 
 
@app.route('/api/delete/book/<id>', methods=['DELETE'])
def delete(id):  
    cpt=0
    for b in books:
        if str(b.id)==id:
            books.pop(cpt)
            break
        cpt=cpt+1
            
    with open(path, 'w') as file:
        file.write("[")
    bAddComma=False
    for book in books:
        book.writeToFile(path, bAddComma)
        bAddComma=True
    print(book)
    
    with open(path, "a") as file:
        file.write("]")
    
    readBooks()
    return "ok"

@app.route('/api/update/book/', methods=['PUT'])
def update():
    data = json.loads(request.data)
    for elm in data:
        for b in books:
            if b.updateFromJson(elm):
                break
    
    with open(path, 'w') as file:
        file.write("[")
    bAddComma=False
    for book in books:
        book.writeToFile(path, bAddComma)
        bAddComma=True
    
    with open(path, "a") as file:
        file.write("]")
    readBooks()
    return "ok"


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)