import React from "react";
import {
  Users,
  ShieldCheck,
  AlertTriangle,
  CalendarDays,
} from "lucide-react";
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";

const data = [
  { name: "Completed", value: 65 },
  { name: "Pending", value: 35 },
];
const COLORS = ["#00C49F", "#FF8042"];

const Dashboard: React.FC = () => {
  const stats = [
    {
      title: "Total Voters",
      value: "12,540",
      icon: <Users className="w-6 h-6 text-blue-500" />,
      color: "bg-blue-50",
    },
    {
      title: "Registered Agents",
      value: "420",
      icon: <ShieldCheck className="w-6 h-6 text-green-500" />,
      color: "bg-green-50",
    },
    {
      title: "Active Incidents",
      value: "8",
      icon: <AlertTriangle className="w-6 h-6 text-red-500" />,
      color: "bg-red-50",
    },
    {
      title: "Events This Week",
      value: "14",
      icon: <CalendarDays className="w-6 h-6 text-purple-500" />,
      color: "bg-purple-50",
    },
  ];

  return (
    <div className="space-y-6">
      {/* Cards Section */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((item, index) => (
          <div
            key={index}
            className={`rounded-xl shadow p-4 flex items-center justify-between ${item.color}`}
          >
            <div>
              <p className="text-gray-600 text-sm">{item.title}</p>
              <h2 className="text-2xl font-semibold mt-1 text-gray-800">
                {item.value}
              </h2>
            </div>
            <div className="p-3 bg-white rounded-lg shadow-inner">
              {item.icon}
            </div>
          </div>
        ))}
      </div>

      {/* Donut Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {[1, 2].map((_, index) => (
          <div
            key={index}
            className="bg-white rounded-xl shadow p-6 flex flex-col items-center"
          >
            <h3 className="text-gray-700 font-semibold mb-4">
              Donut Chart {index + 1}
            </h3>
            <div className="w-full h-64">
              <ResponsiveContainer>
                <PieChart>
                  <Pie
                    data={data}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={90}
                    dataKey="value"
                  >
                    {data.map((entry, i) => (
                      <Cell key={`cell-${i}`} fill={COLORS[i % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
