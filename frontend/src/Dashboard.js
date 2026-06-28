import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import MetricsChart from "./MetricsChart";

const socket = io(
    "https://nethealth-936022305209.us-central1.run.app"
);
const API_URL = "http://localhost:8080";

const startMonitoring = async () => {
    try {
        const response = await fetch(`${API_URL}/api/start-monitoring`, {
            method: "POST",
        });

        const data = await response.json();

        alert(data.message);
    } catch (err) {
        console.error(err);
    }
};
<button
    className="start-btn"
    onClick={startMonitoring}
>
    ▶ Start Monitoring
</button>
const stopMonitoring = async () => {
    const response = await fetch(`${API_URL}/api/stop-monitoring`, {
        method: "POST",
    });

    const data = await response.json();

    alert(data.message);
};
<button
    className="stop-btn"
    onClick={stopMonitoring}
>
    ■ Stop Monitoring
</button>
const [running, setRunning] = useState(false);

useEffect(() => {
    fetchStatus();
}, []);

const fetchStatus = async () => {
    const response = await fetch(`${API_URL}/api/status`);
    const data = await response.json();
    setRunning(data.running);
};
<h3>
    Status: {running ? "🟢 Running" : "🔴 Stopped"}
</h3>


function Dashboard() {
    /*
      Data Structure:
      Array of metric objects
  
      Time Complexity:
      O(n)
    */

    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        // ✅ Initial fetch
        fetch(
            "https://nethealth-936022305209.us-central1.run.app/api/metrics/192.168.1.1"
        )
            .then((res) => res.json())
            .then((data) => {
                setMetrics(data.metrics);
            });

        // ✅ Realtime updates
        socket.on("metrics_update", (data) => {
            setMetrics((prev) => [...data, ...prev].slice(0, 50));
        });

        return () => {
            socket.disconnect();
        };
    }, []);

    return (
        <div>
            <h1>NetHealth Dashboard</h1>

            <MetricsChart data={metrics} />
        </div>
    );
}

export default Dashboard;