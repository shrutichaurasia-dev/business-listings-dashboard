import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  PieChart,
  Pie,
  Cell,
  Legend,
} from "recharts";
import "./styles.css";
import { useEffect, useState } from "react";

export default function App() {
  const [cities, setCities] = useState([]);
  const [categories, setCategories] = useState([]);
  const [sources, setSources] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/city-count")
      .then((response) => response.json())
      .then((data) => {
        setCities(data);
      });

    fetch("http://127.0.0.1:8000/category-count")
      .then((response) => response.json())
      .then((data) => {
        setCategories(data);
      });

    fetch("http://127.0.0.1:8000/source-count")
      .then((response) => response.json())
      .then((data) => {
        setSources(data);
      });
  }, []);

  return (
    <div className="App">
      <h1>Business Listings Dashboard</h1>

      <h2>City Wise Count</h2>
      <div className="chart-container">
        <BarChart width={500} height={300} data={cities}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="city" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#8884d8" />
        </BarChart>
      </div>

      <h2>Category Wise Count</h2>
      <div className="chart-container">
        <PieChart width={400} height={300}>
          <Pie
            data={categories}
            dataKey="count"
            nameKey="category"
            outerRadius={100}
            fill="#82ca9d"
            label
          />
          <Tooltip />
          <Legend />
        </PieChart>
      </div>

      <h2>Source Wise Count</h2>
      <div className="chart-container">
        <BarChart width={500} height={300} data={sources}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="source" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#ff69b4" />
        </BarChart>
      </div>
    </div>
  );
}
