import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

export default function TimelinePlot({ data }) {
  return (
    <LineChart width={800} height={300} data={data}>
      <XAxis dataKey="timestamp" />
      <YAxis />
      <Tooltip />
      <CartesianGrid strokeDasharray="3 3" />
      <Line type="monotone" dataKey="value" stroke="#8884d8" />
      <Line type="monotone" dataKey="anomaly" stroke="red" dot={false} />
    </LineChart>
  );
}
