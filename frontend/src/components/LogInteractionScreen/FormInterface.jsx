import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { addInteraction, setLoading, setError } from '../../redux/interactionSlice'
import { interactionAPI } from '../../services/api'
import { v4 as uuidv4 } from 'uuid'
import './FormInterface.css'

const FormInterface = () => {
  const dispatch = useDispatch()
  const [formData, setFormData] = useState({
    hcp_name: '',
    hcp_id: '',
    interaction_date: new Date().toISOString().split('T')[0],
    interaction_type: 'phone',
    summary: '',
    topics: '',
    outcomes: '',
    next_steps: ''
  })
  const [submitted, setSubmitted] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    dispatch(setLoading(true))

    try {
      const payload = {
        ...formData,
        hcp_id: formData.hcp_id || uuidv4()
      }
      const response = await interactionAPI.create(payload)
      dispatch(addInteraction(response.data))
      setSubmitted(true)
      setFormData({
        hcp_name: '',
        hcp_id: '',
        interaction_date: new Date().toISOString().split('T')[0],
        interaction_type: 'phone',
        summary: '',
        topics: '',
        outcomes: '',
        next_steps: ''
      })
      setTimeout(() => setSubmitted(false), 3000)
    } catch (error) {
      dispatch(setError(error.message))
    } finally {
      dispatch(setLoading(false))
    }
  }

  return (
    <form className="form-interface" onSubmit={handleSubmit}>
      <h2>📋 Log Interaction - Structured Form</h2>

      {submitted && <div className="success-message">✓ Interaction logged successfully!</div>}

      <div className="form-group">
        <label>HCP Name *</label>
        <input
          type="text"
          name="hcp_name"
          value={formData.hcp_name}
          onChange={handleChange}
          required
          placeholder="Enter HCP name"
        />
      </div>

      <div className="form-row">
        <div className="form-group">
          <label>Interaction Date *</label>
          <input
            type="date"
            name="interaction_date"
            value={formData.interaction_date}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Interaction Type *</label>
          <select name="interaction_type" value={formData.interaction_type} onChange={handleChange}>
            <option value="phone">Phone Call</option>
            <option value="in-person">In-Person</option>
            <option value="email">Email</option>
            <option value="virtual">Virtual Meeting</option>
          </select>
        </div>
      </div>

      <div className="form-group">
        <label>Summary *</label>
        <textarea
          name="summary"
          value={formData.summary}
          onChange={handleChange}
          required
          placeholder="Brief summary of the interaction"
          rows="4"
        />
      </div>

      <div className="form-group">
        <label>Topics Discussed</label>
        <input
          type="text"
          name="topics"
          value={formData.topics}
          onChange={handleChange}
          placeholder="Comma-separated topics (e.g., Product A, Outcomes, Pricing)"
        />
      </div>

      <div className="form-group">
        <label>Outcomes</label>
        <textarea
          name="outcomes"
          value={formData.outcomes}
          onChange={handleChange}
          placeholder="What were the results of this interaction?"
          rows="3"
        />
      </div>

      <div className="form-group">
        <label>Next Steps</label>
        <textarea
          name="next_steps"
          value={formData.next_steps}
          onChange={handleChange}
          placeholder="Planned follow-up actions"
          rows="3"
        />
      </div>

      <button type="submit" className="submit-btn">Submit Interaction</button>
    </form>
  )
}

export default FormInterface
