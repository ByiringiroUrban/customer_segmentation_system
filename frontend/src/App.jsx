import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [segment, setSegment] = useState('Consumer')
  const [stateValue, setStateValue] = useState('California')
  const [city, setCity] = useState('Los Angeles')
  const [cluster, setCluster] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)
    setError('')
    setCluster(null)

    try {
      const response = await axios.post('/predict', {
        segment,
        state: stateValue,
        city,
      })

      setCluster(response.data.cluster)
    } catch (err) {
      console.error(err)
      setError('Unable to get prediction. Make sure the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <div className="card">
        <h1>Customer Segmentation</h1>
        <p>Send your customer attributes to the ML backend and see the predicted cluster.</p>

        <form onSubmit={handleSubmit} className="form-grid">
          <label>
            Segment
            <select value={segment} onChange={(e) => setSegment(e.target.value)}>
              <option value="Consumer">Consumer</option>
              <option value="Corporate">Corporate</option>
              <option value="Home Office">Home Office</option>
            </select>
          </label>

          <label>
            State
            <input
              type="text"
              value={stateValue}
              onChange={(e) => setStateValue(e.target.value)}
              placeholder="California"
            />
          </label>

          <label>
            City
            <input
              type="text"
              value={city}
              onChange={(e) => setCity(e.target.value)}
              placeholder="Los Angeles"
            />
          </label>

          <button type="submit" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict Cluster'}
          </button>
        </form>

        {error && <div className="error">{error}</div>}
        {cluster !== null && (
          <div className="result">Predicted Cluster: {cluster}</div>
        )}
      </div>
    </div>
  )
}

export default App
