import React from "react";
import {
  FaTachometerAlt,
  FaUserFriends,
  FaPrint,
  FaUserTie,
  FaUsersCog,
  FaComments,
  FaMoneyBill,
  FaBook,
  FaExclamationTriangle,
  FaDollarSign,
  FaUserShield,
  FaListAlt,
  FaSignOutAlt,
} from "react-icons/fa";

const Sidebar: React.FC = () => {
  const topMenu = [
    { name: "Dashboard", icon: <FaTachometerAlt /> },
    { name: "Voter Search", icon: <FaUserFriends /> },
    { name: "Printable Lists", icon: <FaPrint /> },
    { name: "Agents", icon: <FaUserTie /> },
    { name: "Station Agents", icon: <FaUsersCog /> },
    { name: "Comms", icon: <FaComments /> },
    { name: "Payments", icon: <FaMoneyBill /> },
    { name: "Diary", icon: <FaBook /> },
    { name: "Incidents", icon: <FaExclamationTriangle /> },
    { name: "Finance", icon: <FaDollarSign /> },
  ];

  const bottomMenu = [
    { name: "User Management", icon: <FaUserShield /> },
    { name: "Audit Trail", icon: <FaListAlt /> },
    { name: "Logout", icon: <FaSignOutAlt /> },
  ];

  return (
    <aside className="bg-[#1a1f36] text-white w-64 flex flex-col">
      <div className="text-xl font-bold px-6 py-4 border-b border-gray-700">
        ✅ TEST CMS
      </div>

      <nav className="flex-1 overflow-y-auto p-4 space-y-1">
        {topMenu.map((item, index) => (
          <div
            key={index}
            className="flex items-center space-x-3 px-3 py-2 rounded-md hover:bg-[#2b3152] transition cursor-pointer"
          >
            <span className="text-lg">{item.icon}</span>
            <span className="text-sm font-medium">{item.name}</span>
          </div>
        ))}
      </nav>

      <div className="border-t border-gray-700 p-4 space-y-1">
        {bottomMenu.map((item, index) => (
          <div
            key={index}
            className="flex items-center space-x-3 px-3 py-2 rounded-md hover:bg-[#2b3152] transition cursor-pointer"
          >
            <span className="text-lg">{item.icon}</span>
            <span className="text-sm font-medium">{item.name}</span>
          </div>
        ))}
      </div>
    </aside>
  );
};

export default Sidebar;
