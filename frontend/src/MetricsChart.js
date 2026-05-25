import React from "react";

import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    Legend
} from "recharts";

function MetricsChart({ data }) {

    /*
      Time Complexity:
      O(n)
  
      Data Structure:
      Array of objects
    */

    return (
        <div
            style={{
                padding: "20px"
            }}
        >
            <LineChart
                width={1000}
                height={400}
                data={data}
            >
                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="ts" />

                <YAxis />

                <Tooltip />

                <Legend />

                <Line
                    type="monotone"
                    dataKey="inBytes"
                />

                <Line
                    type="monotone"
                    dataKey="outBytes"
                />
            </LineChart>
        </div>
    );
}

export default MetricsChart;