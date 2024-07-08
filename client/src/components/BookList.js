import BookPage from "./BookPage"

export default function BookList({ books }) {

  return (
    <div className="App">
      <p>booklist here</p>
        <ul>{books.map(book => (
          <BookPage key={book.id} book={book} />
        ))} </ul>
    </div>
  )
}