import React from "react";
import Sidebar from "./components/Navbar";
import Topbar from "./components/Topbar";
import Dashboard from "./pages/Dashboard";


const App: React.FC = () => {
  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Topbar />
        <main className="flex-1 overflow-y-auto p-6">
          <Dashboard />
         

        </main>
      </div>
    </div>
  );
};

export default App;
