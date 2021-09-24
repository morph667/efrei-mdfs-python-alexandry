import { useState, useEffect } from 'react';
import { Modal, Button } from 'react-bootstrap'
import './App.css';

function App() {
    const [data, setData] = useState([])
    const [book, setBook] = useState([])
    const [modalInfo, setModalInfo] = useState(false)
    const [modalAdd, setModalAdd] = useState(false)
    const [newAuthor, setNewAuthor] = useState(false)
    const [newYear, setNewYear] = useState(false)
    const [newType, setNewType] = useState(false)
    const [newGenre, setNewGenre] = useState(false)

    useEffect(() => {
        getData()
        
    }, []);

    const getData = ()=> {
        fetch('api/get/books', {crossDomain: true,
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }})
            .then(response => response.json())
            .then(data => setData(data));
    }

    const addData = ()=> {
        fetch('api/get/books', {crossDomain: true,
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }})
            .then(response => response.json())
            .then(data => setData(data));
    }

    return (
        <div id="mainDiv">
            <Button 
                variant="outline-primary" 
                onClick={() => setModalAdd(!modalAdd)}
                className="libraryTitle"
            >
                Add a book
            </Button>
            <h1 className="libraryTitle">Library :</h1>
            <br/>
            <br/>
            <div id="mainBooksDiv">
                {data.map( (item) => (
                    <div className="booksClass">
                        <div className="bookInfo" onClick={() => {
                            setModalInfo(!modalInfo)
                            setBook(item)
                            }}>
                            <div>
                                <p> Nom : </p> 
                                <p> {item.name}</p>
                            </div>
                            <div style={{marginLeft:"5%"}}>
                                <p> Auteur(s) :</p>
                                <p>{item.authors}</p>
                            </div>
                        </div>
                    <div className="divider"></div>
                    </div>
                ) )}
            </div>

            {modalInfo && (
                <Modal 
                show={modalInfo} 
                onHide={() => setModalInfo(!modalInfo)} size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered >
                    <Modal.Header closeButton>
                        <Modal.Title> <h2 style={{color: "#0D6EFD" }}> {book.name} </h2> </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <h5 style={{marginTop: 10, fontWeight:200, textAlign: 'center'}}>
                            <p style={{fontWeight:"bold"}}> Author(s) :</p> {book.authors.map( author => (
                                    <p> {author} </p>
                                ))}
                            <p style={{fontWeight:"bold",marginTop:"5%"}}> Year :</p> {book.year}
                            <p style={{fontWeight:"bold",marginTop:"5%"}}> Type :</p> {book.type}
                            <p style={{fontWeight:"bold",marginTop:"5%"}}> Genre(s) :</p> {book.genres.map( genre => (
                                <p> {genre} </p>
                            ))}
                            
                        </h5>
                    </Modal.Body>
                </Modal>
            )}

            {modalAdd && (
                <Modal 
                show={modalAdd} 
                onHide={() => setModalAdd(!modalAdd)} size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered >
                    <Modal.Header closeButton>
                        <Modal.Title> <h2 style={{color: "#0D6EFD" }}> Add a book </h2> </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <h5 style={{marginTop: 10, fontWeight:200, textAlign: 'center'}}>
                            <p style={{fontWeight:"bold"}}> Author(s) :</p>
                            <input type="text" name="author" onChange={ () => {}}/>

                            <p style={{fontWeight:"bold",marginTop:"5%"}}> Year :</p> 
                            <input type="number" min="1900" max="2022" name="year"/>

                            <p style={{fontWeight:"bold",marginTop:"5%"}}> Type :</p> 
                            <input type="text" name="type"/>

                            <p style={{fontWeight:"bold",marginTop:"5%"}}> Genre(s) :</p> 
                            <input type="text" name="genre"/>
                            <br/>
                            <br/>
                            <Button 
                                variant="outline-primary" 
                                onClick={() => {
                                    setModalAdd(!modalAdd)
                                    addData()
                                }}
                                className="libraryTitle"
                            >
                                Add this book
                            </Button>
                        </h5>
                    </Modal.Body>
                </Modal>
            )}
        </div>
    );
}

export default App;
