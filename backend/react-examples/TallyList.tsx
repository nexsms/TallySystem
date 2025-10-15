"use client"

// Example React Component for displaying tallies
import { useState, useEffect } from "react"
import { tallyAPI } from "./api-client"

interface Tally {
  id: number
  location: string
  constituency: string
  ward: string
  polling_station: string
  registered_voters: number
  votes_cast: number
  candidate_votes: number
  turnout_percentage: number
  created_at: string
}

export default function TallyList() {
  const [tallies, setTallies] = useState<Tally[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    fetchTallies()
  }, [])

  const fetchTallies = async () => {
    try {
      const data = await tallyAPI.getAll()
      setTallies(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch tallies")
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="text-center py-8">Loading tallies...</div>
  }

  if (error) {
    return <div className="bg-red-100 text-red-700 p-4 rounded">Error: {error}</div>
  }

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Campaign Tallies</h1>

      <div className="grid gap-4">
        {tallies.map((tally) => (
          <div key={tally.id} className="bg-white p-6 rounded-lg shadow-md">
            <div className="flex justify-between items-start mb-4">
              <div>
                <h3 className="text-xl font-semibold">{tally.polling_station}</h3>
                <p className="text-gray-600">
                  {tally.ward}, {tally.constituency}, {tally.location}
                </p>
              </div>
              <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">
                {tally.turnout_percentage.toFixed(1)}% Turnout
              </span>
            </div>

            <div className="grid grid-cols-3 gap-4 text-center">
              <div>
                <p className="text-gray-600 text-sm">Registered</p>
                <p className="text-2xl font-bold">{tally.registered_voters}</p>
              </div>
              <div>
                <p className="text-gray-600 text-sm">Votes Cast</p>
                <p className="text-2xl font-bold">{tally.votes_cast}</p>
              </div>
              <div>
                <p className="text-gray-600 text-sm">Our Votes</p>
                <p className="text-2xl font-bold text-green-600">{tally.candidate_votes}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
