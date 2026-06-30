# NetHealth - Network Performance & Device Health Monitoring System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57)
![Google Cloud Run](https://img.shields.io/badge/Google-Cloud%20Run-4285F4)
![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-181717)

---

## Overview

NetHealth is a full-stack Network Performance & Device Health Monitoring System that simulates enterprise network monitoring.

The application continuously polls simulated network devices, calculates bandwidth utilization, stores metrics in SQLite, generates alerts when thresholds are exceeded, and displays everything through a responsive React dashboard.

Unlike a static dashboard, NetHealth allows users to start and stop live monitoring directly from the web interface.

---

## Features

- Real-time network monitoring simulation
- Start/Stop monitoring from the dashboard
- RESTful Flask API
- SQLite database
- Live bandwidth charts
- Alert management
- Socket.IO WebSocket support
- Google Cloud Run backend
- GitHub Pages frontend
- Responsive dashboard
- Production-ready Docker deployment

---

## Architecture

```
             Simulated Devices
                     │
                     ▼
             Polling Engine
               (main.py)
                     │
                     ▼
        Bandwidth Calculations
             (metrics.py)
                     │
                     ▼
             SQLite Database
            (database.py)
                     │
                     ▼
           Flask REST API
              (app.py)
                     │
          WebSocket Updates
             Socket.IO
                     │
                     ▼
          React Dashboard
     Charts • Alerts • Controls
```

---

# Tech Stack

## Backend

- Python
- Flask
- Flask-SocketIO
- Flask-CORS
- SQLite
- Gunicorn

## Frontend

- React
- Recharts
- Socket.IO Client

## Deployment

- Google Cloud Run
- Docker
- GitHub Pages

---

# Project Structure

```
NetHealth
│
├── backend
│   ├── app.py
│   ├── database.py
│   ├── metrics.py
│   ├── alert_manager.py
│   ├── main.py
│   ├── snmp_client.py
│   ├── socket_manager.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── Dashboard.js
│   │   ├── Alerts.js
│   │   ├── MetricsChart.js
│   │   └── index.js
│   │
│   ├── public
│   └── package.json
│
└── README.md
```

---

# REST API

## Health Check

```
GET /health
```

Response

```json
{
    "status": "healthy"
}
```

---

## Get Metrics

```
GET /api/metrics/<host>
```

Example

```
GET /api/metrics/192.168.1.1
```

Returns

```json
{
    "host": "192.168.1.1",
    "metrics": [...]
}
```

---

## Get Alerts

```
GET /api/alerts
```

---

## Start Monitoring

```
POST /api/start-monitoring
```

Response

```json
{
    "message":"Monitoring started"
}
```

---

## Stop Monitoring

```
POST /api/stop-monitoring
```

---

## Monitoring Status

```
GET /api/status
```

Returns

```json
{
    "running": true
}
```

---

# Running Locally

## Backend

Create virtual environment

```bash
python3 -m venv .venv
```

Activate

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

or

```bash
gunicorn -w 1 -b 0.0.0.0:8080 app:app
```

---

## Frontend

Install dependencies

```bash
npm install
```

Start

```bash
npm start
```

Build

```bash
npm run build
```

Deploy

```bash
npm run deploy
```

---

# Docker

Build

```bash
docker build -t nethealth .
```

Run

```bash
docker run -p 8080:8080 nethealth
```

---

# Google Cloud Run Deployment

Build container

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/nethealth
```

Deploy

```bash
gcloud run deploy nethealth \
--image gcr.io/PROJECT_ID/nethealth \
--platform managed \
--region us-central1 \
--allow-unauthenticated
```

---

# GitHub Pages Deployment

Inside frontend

```bash
npm run deploy
```

The dashboard will be available at

```
https://<username>.github.io/NetHealth/
```

---

# Data Structures Used

| Structure | Usage |
|------------|------|
| Dictionary | API responses |
| List | Metrics & alerts |
| SQLite Tables | Persistent storage |
| React State | UI updates |
| Thread | Background polling |

---

# Time Complexity

| Component | Complexity |
|------------|------------|
| Insert Metric | O(1) |
| Insert Alert | O(1) |
| Query Metrics | O(n) |
| Query Alerts | O(n) |
| Chart Rendering | O(n) |
| Poll Device | O(number of interfaces) |
| Poll Loop | O(number of devices) |

---

# Future Improvements

- SNMP integration with real network devices
- Authentication & role-based access control
- Email/SMS alert notifications
- Historical analytics dashboard
- PostgreSQL support
- Kubernetes deployment
- Prometheus metrics exporter
- Grafana integration
- AI anomaly detection
- Device management interface

---

# Skills Demonstrated

- Full Stack Development
- REST API Design
- React Development
- Python Development
- Flask
- SQLite Database Design
- WebSockets
- Docker
- Google Cloud Platform
- GitHub Pages
- Multithreading
- Data Visualization
- Network Monitoring
- Cloud Deployment
- Software Architecture

---

# Author

**Phillipp Cun**

Computer Science

University of Iowa

LinkedIn:
https://www.linkedin.com/in/pcun

GitHub:
https://github.com/pcun89