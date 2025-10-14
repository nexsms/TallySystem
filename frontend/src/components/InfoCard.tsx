import React from "react";

interface Props {
  title: string;
  value?: string | number | null;
  icon?: React.ReactNode;
  loading?: boolean;
}

export default function InfoCard({ title, value, icon, loading }: Props) {
  return (
    <div className="bg-white rounded-xl p-5 shadow-sm hover:shadow-md transition flex items-center justify-between">
      <div>
        <p className="text-sm text-gray-500">{title}</p>
        <h3 className="text-2xl font-bold text-gray-800 mt-1">
          {loading ? "—" : value ?? "—"}
        </h3>
      </div>
      <div className="p-3 rounded-full bg-indigo-50 text-indigo-600">{icon}</div>
    </div>
  );
}
