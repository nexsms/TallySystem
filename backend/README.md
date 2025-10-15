# Campaign Tally System - Python Backend

A robust FastAPI backend for managing campaign tallies and vote counting for Hon. Philip Aroko 2025.

## Features

- 🔐 **JWT Authentication** - Secure login and registration
- 📊 **Tally Management** - Create, read, update, and delete vote tallies
- 👥 **User Management** - Role-based access control (admin, coordinator, agent, user)
- 📈 **Dashboard Analytics** - Real-time statistics and insights
- 🗳️ **Vote Tracking** - Track votes by location, constituency, and ward
- ✅ **Status Management** - Pending, verified, and disputed tallies

## Installation

1. **Install dependencies:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. **Set up environment variables:**
\`\`\`bash
cp .env.example .env
# Edit .env with your configuration
\`\`\`

3. **Run the server:**
\`\`\`bash
python main.py
\`\`\`

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get access token
- `GET /api/auth/me` - Get current user info

### Tallies
- `POST /api/tallies/` - Create new tally
- `GET /api/tallies/` - Get all tallies (with filters)
- `GET /api/tallies/{id}` - Get specific tally
- `PUT /api/tallies/{id}` - Update tally
- `DELETE /api/tallies/{id}` - Delete tally

### Dashboard
- `GET /api/dashboard/stats` - Get dashboard statistics

### Users
- `GET /api/users/` - Get all users (admin only)
- `GET /api/users/{id}` - Get specific user

## Database Schema

### Users
- Email, username, password (hashed)
- Role (admin, coordinator, agent, user)
- Full name, active status

### Tallies
- Location, constituency, ward
- Vote counts, registered voters
- Turnout percentage
- Status (pending, verified, disputed)
- Creator and timestamps

## Security

- Passwords are hashed using bcrypt
- JWT tokens for authentication
- Role-based access control
- CORS protection

## Usage Example

\`\`\`python
# Register a user
POST /api/auth/register
{
  "email": "agent@campaign.com",
  "username": "agent1",
  "password": "securepass123",
  "full_name": "John Doe"
}

# Login
POST /api/auth/login
username=agent1&password=securepass123

# Create a tally (with Bearer token)
POST /api/tallies/
{
  "location": "Polling Station 001",
  "constituency": "Central",
  "ward": "Ward 5",
  "votes_count": 450,
  "total_registered_voters": 800,
  "notes": "Smooth voting process"
}
\`\`\`

## Production Deployment

For production:
1. Use PostgreSQL instead of SQLite
2. Change `SECRET_KEY` to a secure random string
3. Set up proper CORS origins
4. Use environment variables for all sensitive data
5. Enable HTTPS
6. Set up proper logging and monitoring

## License

MIT
