# Automated Tank Filling System (PLC + OPC UA + Python Dashboard)

## Overview
This project simulates an automated industrial tank filling system using PLC logic and real-time monitoring.

It demonstrates:
- PLC programming using CODESYS
- Industrial communication via OPC UA
- Real-time data acquisition in Python
- Statistical Process Control (SPC)
- Interactive dashboard visualization

---

## System Architecture

Tank Simulation (PLC)
        ↓
Control Logic (Structured Text)
        ↓
OPC UA Server
        ↓
Python Data Logger
        ↓
Streamlit Dashboard

---

## Features

- Automated tank level control with hysteresis
- Valve actuation logic
- Safety interlocks and alarm conditions
- Real-time OPC UA data acquisition
- Live monitoring dashboard
- SPC control chart (mean, UCL, LCL)
- Simulation mode for cloud deployment

---

## Tech Stack

- CODESYS (PLC Simulation)
- OPC UA
- Python
- Streamlit
- Plotly
- Pandas

---

## How to Run Locally

1. Start PLC simulation in CODESYS
2. Ensure OPC UA server is running (`opc.tcp://localhost:4840`)
3. Run:

```bash
streamlit run dashboard/dashboard.py
```

![Demo](PLC%20demo%20media/tank%20sim%20gauge.gif)
![Demo](PLC%20demo%20media/tank%20sim%20trend.gif)
![Demo](PLC%20demo%20media/tank%20sim%20SPC.gif)

