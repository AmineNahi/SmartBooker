import React, { useState } from "react";
import API from "../services/api.js";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await API.post("/auth/login", { email, password });
      localStorage.setItem("token", data.token);
      alert(`Connexion réussie ! Bienvenue ${data.name}`);
    } catch (error) {
      console.log(error.response); // <- très important pour debug
      alert(error.response?.data?.message || "Erreur lors de la connexion");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Connexion</h2>
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      <input type="password" placeholder="Mot de passe" value={password} onChange={(e) => setPassword(e.target.value)} required />
      <button type="submit">Se connecter</button>
    </form>
  );
}
