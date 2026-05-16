import React from "react";

import {
    HashRouter,
    Routes,
    Route,
    Link
} from "react-router-dom";

import Dashboard from "./Dashboard";
import Alerts from "./Alerts";

function App() {
    return (
        <HashRouter>
            <nav
                style={{
                    display: "flex",
                    gap: "20px",
                    padding: "20px",
                    background: "#111",
                    color: "white"
                }}
            >
                <Link
                    style={{ color: "white" }}
                    to="/"
                >
                    Dashboard
                </Link>

                <Link
                    style={{ color: "white" }}
                    to="/alerts"
                >
                    Alerts
                </Link>
            </nav>

            <Routes>
                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/alerts"
                    element={<Alerts />}
                />
            </Routes>
        </HashRouter>
    );
}

export default App;