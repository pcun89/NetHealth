import React, { useEffect, useState } from "react";

function Alerts() {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/api/alerts")
            .then(res => res.json())
            .then(data => setAlerts(data));
    }, []);

    return (
        <div>
            <h1>Alerts</h1>
            {alerts.map((a, i) => (
                <div key={i}>
                    <b>{a.severity}</b> - {a.message}
                </div>
            ))}
        </div>
    );
}

export default Alerts;