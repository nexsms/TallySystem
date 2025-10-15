# React Frontend Integration Guide

This guide shows you how to connect your React frontend to the FastAPI backend.

## Quick Setup

### 1. Environment Variables

Create a `.env` file in your React project root:

\`\`\`env
REACT_APP_API_URL=http://localhost:8000
\`\`\`

For production, update this to your deployed backend URL.

### 2. Install Dependencies

No additional dependencies needed! The examples use native `fetch` API.

If you prefer axios:
\`\`\`bash
npm install axios
\`\`\`

### 3. Backend CORS Configuration

The FastAPI backend is already configured to accept requests from your React app. 

To customize allowed origins, update your backend `.env` file:
\`\`\`env
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173,https://yourdomain.com
\`\`\`

## Usage Examples

### Authentication Flow

\`\`\`tsx
import { authAPI } from './api-client';

// Login
const handleLogin = async () => {
  try {
    const response = await authAPI.login('username', 'password');
    console.log('Logged in:', response);
    // Token is automatically stored in localStorage
  } catch (error) {
    console.error('Login failed:', error);
  }
};

// Get current user
const getCurrentUser = async () => {
  try {
    const user = await authAPI.getCurrentUser();
    console.log('Current user:', user);
  } catch (error) {
    console.error('Not authenticated');
  }
};

// Logout
authAPI.logout();
\`\`\`

### Fetching Tallies

\`\`\`tsx
import { tallyAPI } from './api-client';

// Get all tallies
const tallies = await tallyAPI.getAll();

// Get specific tally
const tally = await tallyAPI.getById(1);

// Create new tally
const newTally = await tallyAPI.create({
  location: 'Nairobi',
  constituency: 'Westlands',
  ward: 'Parklands',
  polling_station: 'Parklands Primary School',
  registered_voters: 1500,
  votes_cast: 1200,
  candidate_votes: 800
});
\`\`\`

### Dashboard Data

\`\`\`tsx
import { dashboardAPI } from './api-client';

// Get overall statistics
const stats = await dashboardAPI.getStats();

// Get data by constituency
const constituencyData = await dashboardAPI.getByConstituency();

// Get data by ward
const wardData = await dashboardAPI.getByWard();
\`\`\`

## Protected Routes

Create a protected route wrapper for authenticated pages:

\`\`\`tsx
import { useEffect, useState } from 'react';
import { authAPI } from './api-client';

export function ProtectedRoute({ children }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      await authAPI.getCurrentUser();
      setIsAuthenticated(true);
    } catch (error) {
      setIsAuthenticated(false);
      window.location.href = '/login';
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  
  return isAuthenticated ? children : null;
}
\`\`\`

## Error Handling

The API client automatically handles errors. You can customize error handling:

\`\`\`tsx
try {
  const data = await tallyAPI.getAll();
} catch (error) {
  if (error.message.includes('401')) {
    // Unauthorized - redirect to login
    authAPI.logout();
    window.location.href = '/login';
  } else {
    // Other errors
    console.error('API Error:', error.message);
  }
}
\`\`\`

## Real-time Updates (Optional)

For real-time tally updates, you can implement polling:

\`\`\`tsx
useEffect(() => {
  const interval = setInterval(async () => {
    const stats = await dashboardAPI.getStats();
    setStats(stats);
  }, 5000); // Update every 5 seconds

  return () => clearInterval(interval);
}, []);
\`\`\`

## API Documentation

Your FastAPI backend provides interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

Use these to explore all available endpoints and test API calls.

## Deployment

### Backend Deployment
Deploy your FastAPI backend to:
- Vercel (recommended)
- Railway
- Render
- AWS/GCP/Azure

### Frontend Deployment
Deploy your React app to:
- Vercel (recommended)
- Netlify
- GitHub Pages

Update `REACT_APP_API_URL` to point to your production backend URL.
\`\`\`

```python file="" isHidden
