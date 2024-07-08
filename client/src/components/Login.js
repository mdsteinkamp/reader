import { useState } from "react"

export default function Login() {
  const [formData, setFormData] = useState({username: ""})

  function handleChange(e) {
    const name = e.target.name
    const value = e.target.value
    setFormData({
      ...formData,
      [name]: value
    })
  }

  console.log(formData)

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const response = await fetch('http://127.0.0.1:8000//api/users', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
      const user = await response.json()
      console.log(user)
    } catch(e) {
      console.log(e)
    }
  }

  return (
    <div>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
        />
        <button>Sign In</button>
      </form>
    </div>

  )
}