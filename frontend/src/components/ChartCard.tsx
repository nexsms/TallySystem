import React from "react";
import { ResponsiveContainer, PieChart, Pie, Cell, Legend } from "recharts";

interface ChartCardProps {
  title: string;
  data: { name: string; value: number }[];
  colors?: string[];
  height?: number;
}

export default function ChartCard({
  title,
  data,
  colors = ["#4f46e5", "#ec4899", "#fbbf24"],
  height = 220,
}: ChartCardProps) {
  return (
    <div className="bg-white rounded-xl p-5 shadow-sm">
      <h3 className="font-semibold text-gray-800 mb-4">{title}</h3>
      <div style={{ width: "100%", height }}>
        <ResponsiveContainer>
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              innerRadius={50}
              outerRadius={80}
              paddingAngle={4}
            >
              {data.map((_, i) => (
                <Cell key={i} fill={colors[i % colors.length]} />
              ))}
            </Pie>
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
