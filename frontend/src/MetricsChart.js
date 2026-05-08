import React from "react";
import {
    LineChart, Line, XAxis, YAxis, Tooltip
} from "recharts";

function MetricsChart({ data }) {
    return (
        <LineChart width={600} height={300} data={data}>
            <XAxis dataKey="ts" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="inBytes" />
            <Line type="monotone" dataKey="outBytes" />
        </LineChart>
    );
}

export default MetricsChart;