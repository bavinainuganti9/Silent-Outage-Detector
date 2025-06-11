import React, { useState } from "react";
import axios from "axios";
import TimelinePlot from "./Components/TimelinePlot";

export default function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);

  const upload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("column", "value");
    formData.append("method", "zscore");
    const res = await axios.post("http://localhost:8000/analyze/", formData);
    setData(res.data);
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">SilentScope – Silent Outage Detector</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={upload} className="bg-blue-600 text-white px-4 py-2 mt-2">Analyze</button>
      <div className="mt-6">
        <TimelinePlot data={data} />
      </div>
    </div>
  );
}
