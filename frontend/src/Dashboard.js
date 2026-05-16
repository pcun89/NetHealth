import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import MetricsChart from "./MetricsChart";

const socket = io(
    "https://nethealth-936022305209.us-central1.run.app"
);

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