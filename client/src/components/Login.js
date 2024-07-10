import { useState, useEffect } from "react"

export default function Login() {
  const [formData, setFormData] = useState({username: ""})
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [csrf, setCsrf] = useState('')

  console.log(isAuthenticated)

  useEffect(() => {
    const getSession = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/session/", {
          credentials: 'include',
        })
        const data = await response.json()
        console.log(data)
        if (data.isAuthenticated) {
          setIsAuthenticated(true)
        } else {
          setIsAuthenticated(false)
          getCSRF()
        }
        // setBooks(books)
      } catch (err) {
        console.log('Error occured when fetching session');
      }
    }
    getSession()
  }, [])

  function getCSRF() {
    fetch("http://127.0.0.1:8000/api/csrf/", {
      credentials: 'include',
    })
    .then(res => {
      console.log(res)
      let csrfToken = res.headers.get("X-CSRFToken")
      setCsrf(csrfToken)
      // console.log(csrf, csrfToken)
    })
    .catch(e => console.log(e))
  }

  function whoami() {
    fetch("http://127.0.0.1:8000/api/whoami/", {
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
    })
  }

  function handleLogout() {
    fetch("http://127.0.0.1:8000/api/logout/", {
      credentials: "include",
    })
    .then(data => {
      console.log(data)
    })
  }

  function handleChange(e) {
    const name = e.target.name
    const value = e.target.value
    setFormData({
      ...formData,
      [name]: value
    })
  }

  console.log(formData)

  const handleLogin = async (e) => {
    e.preventDefault()
    try {
      console.log(csrf)
      const response = await fetch('http://127.0.0.1:8000/api/login/', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrf,
        },
        credentials: 'include',
        body: JSON.stringify(formData)
      })
      const user = await response.json()
      console.log(user)
    } catch(err) {
      console.log(err)
    }
  }

  if(!isAuthenticated) {
    return (
      <div>
        <h1>Sign In</h1>
        <form onSubmit={handleLogin}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
          />
          <input
            type="text"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
          />
          <button>Sign In</button>
        </form>
      </div>
  
    )
  } else {
    return (
      <div>
        <h1>React Cookie Auth</h1>
        <p>you are logged in!</p>
        <button onClick={whoami}>Who Am I?</button>
        <button onClick={handleLogout}>Log Out</button>
      </div>
    )

  }

}