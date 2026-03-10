import { useState } from 'react'
import './App.css'

function App() {
  const [formData, setFormData] = useState({
    fico_range_low: 700,
    annual_inc: 48000,
    dti: 20.0,
    loan_amnt: 9000,
    revol_bal: 5000
  })

  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: parseFloat(value) || 0
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      // Connect to Flask Backend
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Failed to get prediction')
      }

      setResult(data.probability)
    } catch (err) {
      console.error('Error fetching prediction:', err)
      setError(err.message || 'An error occurred while fetching the prediction.')
    } finally {
      setLoading(false)
    }
  }

  const getResultDetails = (prob) => {
    if (prob >= 0.7) {
      return {
        className: 'card-approved',
        color: 'var(--success-border)',
        title: '✅ High Chance of Approval',
        text: 'Your profile looks strong. You have excellent odds of being approved for this loan.'
      }
    } else if (prob >= 0.4) {
      return {
        className: 'card-neutral',
        color: 'var(--warning-border)',
        title: '⚠️ Moderate Chance of Approval',
        text: 'Your approval odds are fair. Additional documentation or a co-signer might help improve your chances.'
      }
    } else {
      return {
        className: 'card-rejected',
        color: 'var(--danger-border)',
        title: '🚫 Low Chance of Approval',
        text: 'Your current profile poses a higher credit risk. Consider improving your FICO score or reducing your debt before applying.'
      }
    }
  }

  return (
    <div className="app-container">
      <div className="card">
        <header>
          <h1 className="title">🏦 Credit Risk Assessment</h1>
          <p className="subtitle">Predict your loan approval odds with AI-powered financial evaluation.</p>
        </header>

        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            {/* Personal Credit Column */}
            <div className="column">
              <div className="section-title">Personal Credit</div>
              
              <div className="input-group">
                <label htmlFor="fico_range_low" className="input-label">FICO Credit Score</label>
                <input
                  type="number"
                  id="fico_range_low"
                  name="fico_range_low"
                  className="input-field"
                  required
                  min="300"
                  max="850"
                  value={formData.fico_range_low}
                  onChange={handleChange}
                />
                <div className="helper-text">A score between 300 and 850.</div>
              </div>
              
              <div className="input-group">
                <label htmlFor="annual_inc" className="input-label">Annual Income ($)</label>
                <input
                  type="number"
                  id="annual_inc"
                  name="annual_inc"
                  className="input-field"
                  required
                  min="0"
                  step="0.01"
                  value={formData.annual_inc}
                  onChange={handleChange}
                />
                <div className="helper-text">Your total yearly gross income.</div>
              </div>
              
              <div className="input-group">
                <label htmlFor="dti" className="input-label">Debt-to-Income Ratio (%)</label>
                <input
                  type="number"
                  id="dti"
                  name="dti"
                  className="input-field"
                  required
                  min="0"
                  max="100"
                  step="0.01"
                  value={formData.dti}
                  onChange={handleChange}
                />
                <div className="helper-text">Monthly debt payments divided by gross monthly income.</div>
              </div>
            </div>

            {/* Loan Details Column */}
            <div className="column">
              <div className="section-title">Loan Details</div>
              
              <div className="input-group">
                <label htmlFor="loan_amnt" className="input-label">Loan Amount ($)</label>
                <input
                  type="number"
                  id="loan_amnt"
                  name="loan_amnt"
                  className="input-field"
                  required
                  min="0"
                  step="0.01"
                  value={formData.loan_amnt}
                  onChange={handleChange}
                />
                <div className="helper-text">Total amount of requested loan.</div>
              </div>
              
              <div className="input-group">
                <label htmlFor="revol_bal" className="input-label">Revolving Balance ($)</label>
                <input
                  type="number"
                  id="revol_bal"
                  name="revol_bal"
                  className="input-field"
                  required
                  min="0"
                  step="0.01"
                  value={formData.revol_bal}
                  onChange={handleChange}
                />
                <div className="helper-text">Total unpaid balance on credit cards and lines of credit.</div>
              </div>
            </div>
          </div>

          <button type="submit" className="btn-predict" disabled={loading}>
            <span>{loading ? 'Analyzing profile...' : '🔮 Predict Approval Odds'}</span>
            {loading && <div className="loader"></div>}
          </button>
        </form>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {/* Results Section */}
        {result !== null && !error && (() => {
          const details = getResultDetails(result)
          return (
            <div className="result-section">
              <h2 className="section-title">📈 Assessment Result</h2>
              
              <div className="metric-container">
                <div className="metric-label">Approval Probability</div>
                <div className="metric-value">{(result * 100).toFixed(1)}%</div>
              </div>

              <div className="progress-bar-bg">
                <div 
                  className="progress-bar-fill" 
                  style={{ 
                    width: `${result * 100}%`,
                    backgroundColor: details.color 
                  }}
                ></div>
              </div>

              <div className={`result-card ${details.className}`}>
                <h4 className="result-title">{details.title}</h4>
                <p className="result-text">{details.text}</p>
              </div>
            </div>
          )
        })()}

        <footer>
          Developed by Mohamed Errakraki | Powered by Machine Learning and React
        </footer>
      </div>
    </div>
  )
}

export default App
