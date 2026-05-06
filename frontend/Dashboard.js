import React, { useEffect, useState } from "react";
import MetricsChart from "./MetricsChart";

function Dashboard() {
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/api/metrics/192.168.1.1")
            .then(res => res.json())
            .then(data => setMetrics(data.metrics));
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            <MetricsChart data={metrics} />
        </div>
    );
}

export default Dashboard;