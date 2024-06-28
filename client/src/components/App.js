import { useState, useEffect } from 'react'
import '../App.css';

export default function App() {
  const [books, setBooks] = useState([])

  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000//api/books")
  //   .then(resp => resp.json())
  //   .then(books => setBooks(books))
  // }, [])

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000//api/books")
        const books = await response.json()
        setBooks(books)
      } catch (err) {
        console.log('Error occured when fetching books');
      }
    }
    fetchBooks()
  }, [])

  console.log(books)

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Lets go!
        </p>

      </header>
    </div>
  );
}