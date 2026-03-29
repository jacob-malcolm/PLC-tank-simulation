# Automated Tank Filling System (PLC + OPC UA + Python Dashboard)

## Overview
This project simulates an automated industrial tank filling system using PLC logic and real-time monitoring.

It demonstrates:  
- PLC programming using CODESYS with **PID control** for smooth tank filling  
- Industrial communication via OPC UA  
- Real-time data acquisition in Python
- Historian-style logging via SQLite
- Statistical Process Control (SPC)  
- Interactive dashboard visualization with gauges and trend charts  

---
![Demo](PLC%20demo%20media/PID%20demo.gif)

## System Architecture

PLC Simulation (CODESYS)
        │
        │  OPC UA
        ▼
Python OPC UA Client
        │
        ├── Real-Time Control Monitoring
        ├── Data Logger (SQLite)
        ▼
SQLite Database (Historical Data)
        │
        ▼
Streamlit Dashboard (HMI / Analytics Layer)
        │
        ├── Live Metrics
        ├── SPC Charts
        ├── Gauge Visualization
        └── Operator Controls (Manual Mode / Reset)

---

## Features

- **PID-based tank level control** for continuous flow adjustment  
- Valve actuation based on PID output  
- Safety interlocks and alarm conditions  
- Real-time OPC UA data acquisition
- Data is continuously written to an SQLite database 
- Live monitoring dashboard:  
  - Tank level trend  
  - SPC control chart (mean, UCL, LCL)  
  - PID valve gauge  
- Simulation mode for cloud deployment without PLC  

---

## Tech Stack

- CODESYS (PLC Simulation)  
- OPC UA  
- Python
- SQLite
- Streamlit  
- Plotly  
- Pandas  

---

## How to Run Locally

1. Start the PLC simulation in CODESYS (with PID logic in `tank_controller.st`)  
2. Ensure OPC UA server is running (`opc.tcp://localhost:4840`)  
3. Run the dashboard:

```bash
streamlit run dashboard/dashboard.py
```
![Demo](PLC%20demo%20media/tank%20sim%20gauge.gif)
![Demo](PLC%20demo%20media/tank%20sim%20trend.gif)
![Demo](PLC%20demo%20media/tank%20sim%20SPC.gif)

