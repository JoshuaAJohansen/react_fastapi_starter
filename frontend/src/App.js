import logo from './logo.svg';
import { useState, useEffect } from 'react';
import './App.css';

import axios from 'axios';

function App() {
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const getResults = async () => {
      setLoading(true)

      try {
        const response = await axios.get(`http://localhost:8000/items/`);
        console.log(response)
        setResults(response.data)
      } catch (err) {
        setError(err)
      }

      setLoading(false)
    };

    getResults();
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome Fastapi
        </p>

        {loading ? (
          <p>loading...</p>
          ) : (
            <ul>
              {results.map(result => (
                <li key={result.id}>
                  <p>{result.name}</p>
                  <p>{result.description}</p>
                </li>
              ))}
            </ul>
          )
            }
        {error && <div>{error.message}</div>}
      </header>
    </div>
  );
}

export default App;
