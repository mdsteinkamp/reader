import { useState, useEffect } from 'react'
import '../App.css';

export default function App() {
  const [books, setBooks] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/api/books")
    .then(resp => resp.json())
    .then(books => setBooks(books))
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