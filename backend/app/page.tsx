// This is a Python FastAPI backend project
// The React examples are in the /react-examples folder for reference only
//
// To use this backend with React:
// 1. Create a separate React project (using create-react-app, Vite, or Next.js)
// 2. Copy the files from /react-examples into your React project
// 3. Start this Python backend: python main.py
// 4. Start your React frontend and it will connect to this backend
//
// For now, this page just shows the project structure

export default function Page() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Campaign Tally System - FastAPI Backend</h1>

          <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-6">
            <p className="text-yellow-800 font-semibold">This is a Python FastAPI backend project, not a React app.</p>
          </div>

          <div className="space-y-6">
            <section>
              <h2 className="text-2xl font-semibold text-gray-800 mb-3">Backend Structure</h2>
              <div className="bg-gray-50 rounded p-4 font-mono text-sm">
                <div>📁 Python Backend Files:</div>
                <div className="ml-4 mt-2 space-y-1">
                  <div>├── main.py (FastAPI app)</div>
                  <div>├── config.py (Configuration)</div>
                  <div>├── database.py (Database setup)</div>
                  <div>├── models.py (SQLAlchemy models)</div>
                  <div>├── schemas.py (Pydantic schemas)</div>
                  <div>├── auth_utils.py (JWT authentication)</div>
                  <div>└── routers/ (API endpoints)</div>
                </div>
              </div>
            </section>

            <section>
              <h2 className="text-2xl font-semibold text-gray-800 mb-3">How to Use</h2>
              <ol className="list-decimal list-inside space-y-2 text-gray-700">
                <li>
                  Start the Python backend:
                  <code className="ml-2 bg-gray-100 px-2 py-1 rounded">python main.py</code>
                </li>
                <li>
                  Backend runs at:
                  <a
                    href="http://localhost:8000"
                    className="ml-2 text-blue-600 hover:underline"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    http://localhost:8000
                  </a>
                </li>
                <li>
                  API docs available at:
                  <a
                    href="http://localhost:8000/docs"
                    className="ml-2 text-blue-600 hover:underline"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    http://localhost:8000/docs
                  </a>
                </li>
                <li>Create a separate React project for the frontend</li>
                <li>
                  Copy files from <code className="bg-gray-100 px-2 py-1 rounded">/react-examples</code> to your React
                  project
                </li>
              </ol>
            </section>

            <section>
              <h2 className="text-2xl font-semibold text-gray-800 mb-3">React Integration</h2>
              <p className="text-gray-700 mb-3">
                The <code className="bg-gray-100 px-2 py-1 rounded">/react-examples</code> folder contains:
              </p>
              <ul className="list-disc list-inside space-y-1 text-gray-700 ml-4">
                <li>api-client.ts - API client for making requests</li>
                <li>LoginForm.tsx - Example login component</li>
                <li>TallyList.tsx - Example tally display</li>
                <li>Dashboard.tsx - Example dashboard</li>
              </ul>
              <p className="text-gray-700 mt-3">
                See <code className="bg-gray-100 px-2 py-1 rounded">REACT_INTEGRATION.md</code> for detailed setup
                instructions.
              </p>
            </section>

            <section className="bg-blue-50 rounded-lg p-6">
              <h2 className="text-2xl font-semibold text-blue-900 mb-3">Quick Start</h2>
              <div className="space-y-2 text-blue-800">
                <p>
                  1. Install dependencies:{" "}
                  <code className="bg-white px-2 py-1 rounded">pip install -r requirements.txt</code>
                </p>
                <p>2. Copy .env.example to .env and update values</p>
                <p>
                  3. Run: <code className="bg-white px-2 py-1 rounded">python main.py</code>
                </p>
                <p>4. Visit the API docs to test endpoints</p>
              </div>
            </section>
          </div>
        </div>
      </div>
    </div>
  )
}
