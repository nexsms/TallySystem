"use client"

// Example React Dashboard Component
import { useState, useEffect } from "react"
import { dashboardAPI } from "./api-client"

interface DashboardStats {
  total_tallies: number
  total_registered_voters: number
  total_votes_cast: number
  total_candidate_votes: number
  overall_turnout: number
  candidate_vote_share: number
}

export default function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchStats()
  }, [])

  const fetchStats = async () => {
    try {
      const data = await dashboardAPI.getStats()
      setStats(data)
    } catch (err) {
      console.error("Failed to fetch stats:", err)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="text-center py-8">Loading dashboard...</div>
  }

  if (!stats) {
    return <div>No data available</div>
  }

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-8">Campaign Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-gray-600 text-sm mb-2">Total Tallies</h3>
          <p className="text-4xl font-bold">{stats.total_tallies}</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-gray-600 text-sm mb-2">Registered Voters</h3>
          <p className="text-4xl font-bold">{stats.total_registered_voters.toLocaleString()}</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-gray-600 text-sm mb-2">Votes Cast</h3>
          <p className="text-4xl font-bold">{stats.total_votes_cast.toLocaleString()}</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-gray-600 text-sm mb-2">Our Votes</h3>
          <p className="text-4xl font-bold text-green-600">{stats.total_candidate_votes.toLocaleString()}</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-gray-600 text-sm mb-2">Overall Turnout</h3>
          <p className="text-4xl font-bold text-blue-600">{stats.overall_turnout.toFixed(1)}%</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-gray-600 text-sm mb-2">Vote Share</h3>
          <p className="text-4xl font-bold text-purple-600">{stats.candidate_vote_share.toFixed(1)}%</p>
        </div>
      </div>
    </div>
  )
}
