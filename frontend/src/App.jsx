import { useState, useEffect } from 'react'
import './App.css'
import { fetchItems, createItem, updateItem, deleteItem, healthCheck } from './services/api'

function App() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [healthStatus, setHealthStatus] = useState(null)
  const [formData, setFormData] = useState({ name: '', description: '' })
  const [editingId, setEditingId] = useState(null)

  useEffect(() => {
    checkHealth()
    loadItems()
  }, [])

  const checkHealth = async () => {
    try {
      const response = await healthCheck()
      setHealthStatus(response.data)
    } catch (err) {
      setHealthStatus({ status: 'error', message: 'Backend not reachable' })
    }
  }

  const loadItems = async () => {
    try {
      setLoading(true)
      const response = await fetchItems()
      setItems(response.data)
      setError(null)
    } catch (err) {
      setError('Failed to load items. Make sure the backend is running.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!formData.name.trim()) return

    try {
      if (editingId) {
        await updateItem(editingId, formData)
      } else {
        await createItem(formData)
      }
      setFormData({ name: '', description: '' })
      setEditingId(null)
      loadItems()
    } catch (err) {
      setError('Failed to save item')
      console.error(err)
    }
  }

  const handleEdit = (item) => {
    setFormData({ name: item.name, description: item.description })
    setEditingId(item.id)
  }

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this item?')) return

    try {
      await deleteItem(id)
      loadItems()
    } catch (err) {
      setError('Failed to delete item')
      console.error(err)
    }
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>SiteStore</h1>
          <p className="subtitle">React + Django Full Stack Application</p>
          {healthStatus && (
            <div className={`health-status ${healthStatus.status === 'healthy' ? 'healthy' : 'error'}`}>
              Backend: {healthStatus.message || healthStatus.status}
            </div>
          )}
        </header>

        <div className="content">
          <div className="form-section">
            <h2>{editingId ? 'Edit Item' : 'Add New Item'}</h2>
            <form onSubmit={handleSubmit} className="form">
              <input
                type="text"
                placeholder="Item name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                className="input"
                required
              />
              <textarea
                placeholder="Description (optional)"
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                className="textarea"
                rows="3"
              />
              <div className="form-actions">
                <button type="submit" className="btn btn-primary">
                  {editingId ? 'Update' : 'Add'} Item
                </button>
                {editingId && (
                  <button
                    type="button"
                    onClick={() => {
                      setFormData({ name: '', description: '' })
                      setEditingId(null)
                    }}
                    className="btn btn-secondary"
                  >
                    Cancel
                  </button>
                )}
              </div>
            </form>
          </div>

          <div className="items-section">
            <h2>Items List</h2>
            {error && <div className="error-message">{error}</div>}
            {loading ? (
              <div className="loading">Loading items...</div>
            ) : items.length === 0 ? (
              <div className="empty-state">No items yet. Add one above!</div>
            ) : (
              <div className="items-grid">
                {items.map((item) => (
                  <div key={item.id} className="item-card">
                    <h3>{item.name}</h3>
                    {item.description && <p>{item.description}</p>}
                    <div className="item-meta">
                      <small>
                        Created: {new Date(item.created_at).toLocaleDateString()}
                      </small>
                    </div>
                    <div className="item-actions">
                      <button
                        onClick={() => handleEdit(item)}
                        className="btn btn-small btn-edit"
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => handleDelete(item.id)}
                        className="btn btn-small btn-delete"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App

