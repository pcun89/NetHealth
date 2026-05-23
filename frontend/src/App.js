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
            <div>
                <nav
                    style={{
                        padding: "20px",
                        background: "#111",
                        display: "flex",
                        gap: "20px"
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
            </div>
        </HashRouter>
    );
}

export default App;