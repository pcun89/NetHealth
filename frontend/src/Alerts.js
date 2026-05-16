import React, { useEffect, useState } from "react";

function Alerts() {
    /*
      Data Structure:
      Array of alert objects
  
      Time Complexity:
      O(n)
    */

    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        fetch(
            "https://nethealth-936022305209.us-central1.run.app/api/alerts"
        )
            .then((res) => res.json())
            .then((data) => {
                setAlerts(data);
            });
    }, []);

    return (
        <div style={{ padding: "20px" }}>
            <h1>System Alerts</h1>

            {alerts.map((alert, index) => (
                <div
                    key={index}
                    style={{
                        border: "1px solid #ccc",
                        marginBottom: "10px",
                        padding: "10px"
                    }}
                >
                    <h3>{alert.severity}</h3>

                    <p>{alert.message}</p>

                    <small>{alert.ts}</small>
                </div>
            ))}
        </div>
    );
}

export default Alerts;