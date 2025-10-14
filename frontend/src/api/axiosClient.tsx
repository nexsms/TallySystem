import axios from "axios";

const axiosClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000", // change when backend ready
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 10000,
});

export default axiosClient;
