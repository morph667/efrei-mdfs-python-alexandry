from flask import Flask, render_template, jsonify, request
import json, os
from book import *



app = Flask(__name__)
path="./data.json"
books = []

def readBooks():
    with open(path, "r") as file:
        data = file.read()
        data = json.loads(data)
        for b in data:
            books.append(Book(b))
            
readBooks()


@app.route('/api/get/books/')
def getBooks():
    string = "" 
    for book in books:
        string+= book.toString() + "<br>"
    print(string)
    return string

@app.route('/api/get/book/<id>')
def getBook(id):
    string = "" 
    
    with open(path, "r") as file:
        data = file.read()
        data = json.loads(data)
        for b in data:
            
            if str(b["id"]) == id:  
                books.append(Book(b))

    for book in books:
        string+= book.toString() + "<br>"
    print(string)
    return string
        
        
        
@app.route('/api/post/book/')
def setBook():
    
    
    with open(path, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        
    data= json.loads(request.data)
    for i in data:
        book= Book(i)
        book.writeToFile(path, True)
        print(i) 
        
    with open(path, "a") as file:
        file.write("\n]")
   
    readBooks()       
    return "ok"

@app.route('/api/post/book/')
def setBook():
     
    with open(path, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        
    data= json.loads(request.data)
    for i in data:
        book= Book(i)
        book.writeToFile(path, True)
        print(i) 
        
    with open(path, "a") as file:
        file.write("\n]")
   
             
    return "ok"
    
        
        
@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)