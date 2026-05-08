import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import MetricsChart from "./MetricsChart";

const socket = io("http://localhost:5000");

function Dashboard() {
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        socket.on("metrics_update", (data) => {
            setMetrics(prev => [...data, ...prev].slice(0, 50));
        });

        return () => socket.disconnect();
    }, []);

    return (
        <div>
            <h1>Live Dashboard</h1>
            <MetricsChart data={metrics} />
        </div>
    );
}

export default Dashboard;