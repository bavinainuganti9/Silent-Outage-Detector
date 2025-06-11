# Silent Outage Detector

## Overview / Description  
SilentScope is a full-stack application that detects silent outages in distributed systems by analyzing logs and system metrics for subtle anomalies that typical alerts might miss. It helps SREs and infrastructure teams proactively identify performance degradations and unexpected behavior using statistical and machine learning techniques.

## Features  
- Upload log or metric time series data as CSV files  
- Detect anomalies using Z-Score and IsolationForest algorithms  
- Identify alert gaps, missing metrics, and silent failures  
- Visualize anomalies over time with an interactive timeline plot  

## Architecture  
Backend: Python FastAPI app for CSV ingestion, anomaly detection, and API exposure  
Anomaly Detection: Statistical (Z-Score) and ML-based (IsolationForest) methods using scikit-learn  
Frontend: React + Recharts + Tailwind CSS for data visualization and UI  
Data Input: CSV files containing timestamped metric values  

## Tech Stack  
Backend: Python, FastAPI, Pandas, Scikit-learn  
Frontend: React, Recharts, Tailwind CSS  
