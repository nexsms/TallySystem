import React from "react";
import { FaUserCircle, FaBell } from "react-icons/fa";

const Topbar: React.FC = () => {
  return (
    <header className="flex justify-between items-center bg-white shadow px-6 py-3 sticky top-0 z-10">
      <h1 className="text-xl font-semibold text-gray-800">Dashboard</h1>

      <div className="flex items-center space-x-6">
        <button className="text-gray-600 hover:text-gray-800 transition">
          <FaBell size={18} />
        </button>
        <div className="flex items-center space-x-2 cursor-pointer">
          <FaUserCircle size={24} className="text-gray-600" />
          <span className="text-gray-700 font-medium">Admin</span>
        </div>
      </div>
    </header>
  );
};

export default Topbar;
