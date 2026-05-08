import React from "react";
import { HashRouter, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./Dashboard";
import Alerts from "./Alerts";

function App() {
    return (
        <HashRouter>
            <nav>
                <Link to="/">Dashboard</Link>
                <Link to="/alerts">Alerts</Link>
            </nav>

            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/alerts" element={<Alerts />} />
            </Routes>
        </HashRouter>
    );
}

export default App;