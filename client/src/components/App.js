import { useState, useEffect } from 'react'
import { Route, Routes } from "react-router-dom"
import '../App.css';
import NavBar from './NavBar';
import Home from './Home';
import BookList from './BookList';

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
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/books" element={<BookList />} />
      </Routes>
    </div>
  );
}