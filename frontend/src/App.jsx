import React, { useState } from "react";
import Register from "./pages/Register.jsx";
import Login from "./pages/Login.jsx";

export default function App() {
  const [page, setPage] = useState("register");

  return (
    <div className="container">
      <nav>
        <button onClick={() => setPage("register")}>Inscription</button>
        <button onClick={() => setPage("login")}>Connexion</button>
      </nav>

      {page === "register" && <Register />}
      {page === "login" && <Login />}
    </div>
  );
}
