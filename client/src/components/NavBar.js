import { NavLink } from "react-router-dom"

export default function NavBar() {


  return(
    <header>
      <NavLink to="/login">Login</NavLink>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/books">My Books</NavLink>

    </header>
  )
}