import { useEffect, useState } from "react";
import api from "./services/api";
import "./App.css";

function App() {
  const [status, setStatus] = useState("Conectando à API...");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function verificarAPI() {
      try {
        const response = await api.get("/health");

        setStatus(response.data.message);
      } catch (error) {
        console.error("Erro ao conectar à API:", error);

        setStatus("Não foi possível conectar à API");
      } finally {
        setLoading(false);
      }
    }

    verificarAPI();
  }, []);

  return (
    <main className="app-container">
      <h1>Passe</h1>

      <p>Sistema de Gestão de Liga de Futebol</p>

      <section className="status-card">
        <h2>Status da conexão</h2>

        {loading ? (
          <p>Verificando conexão...</p>
        ) : (
          <p>{status}</p>
        )}
      </section>
    </main>
  );
}

export default App;
