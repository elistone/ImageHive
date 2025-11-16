import { useState } from 'react';
import './App.css';

interface ApiStatus {
  name: string;
  version: string;
  status: string;
}

function App() {
  const [apiStatus, setApiStatus] = useState<ApiStatus | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const checkApiStatus = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('/api/');
      if (!response.ok) {
        throw new Error('Failed to fetch API status');
      }
      const data = await response.json();
      setApiStatus(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🖼️ ImageHive</h1>
        <p>Modern Image Management & Organization</p>
      </header>

      <main className="App-main">
        <section className="status-section">
          <h2>API Status</h2>
          <button onClick={checkApiStatus} disabled={loading}>
            {loading ? 'Checking...' : 'Check API Connection'}
          </button>
          
          {error && (
            <div className="error">
              <p>❌ Error: {error}</p>
              <p className="error-hint">Make sure the backend server is running on port 8000</p>
            </div>
          )}
          
          {apiStatus && (
            <div className="status-info">
              <p>✅ Connected to {apiStatus.name}</p>
              <p>Version: {apiStatus.version}</p>
              <p>Status: {apiStatus.status}</p>
            </div>
          )}
        </section>

        <section className="features-section">
          <h2>Features (Coming Soon)</h2>
          <div className="features-grid">
            <div className="feature-card">
              <h3>📁 Image Scanning</h3>
              <p>Recursively scan directories for images</p>
            </div>
            <div className="feature-card">
              <h3>🖼️ Thumbnail Gallery</h3>
              <p>Browse images with auto-generated thumbnails</p>
            </div>
            <div className="feature-card">
              <h3>🔍 Deduplication</h3>
              <p>Find and manage duplicate images</p>
            </div>
            <div className="feature-card">
              <h3>🏷️ Smart Tagging</h3>
              <p>AI-powered image tagging and organization</p>
            </div>
          </div>
        </section>
      </main>

      <footer className="App-footer">
        <p>ImageHive - Built with FastAPI + React + TypeScript</p>
      </footer>
    </div>
  );
}

export default App;
