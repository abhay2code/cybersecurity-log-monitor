# 🔐 Cybersecurity Log Monitoring & Threat Detection System

An end-to-end cybersecurity project that analyzes authentication logs, detects suspicious activities such as brute-force attacks and credential compromise, and visualizes security alerts through a web-based dashboard.

---

## 🚀 Features
- Log parsing and analysis using Python  
- Brute-force attack detection based on failed login attempts  
- Detection of successful login after multiple failures (credential compromise)  
- Alert severity classification (HIGH, CRITICAL)  
- Persistent alert storage using SQLite  
- Backend API to serve alerts  
- Web-based dashboard for real-time alert visualization  

---

## 🛠 Tech Stack
- **Python** – Log analysis, threat detection, backend API  
- **JavaScript** – Dashboard data fetching and rendering  
- **HTML/CSS** – Dashboard UI  
- **SQLite** – Alert storage  

---

## 🧩 Project Architecture
1. Authentication logs are read from a log file  
2. Python analyzer detects suspicious patterns  
3. Alerts are stored in a SQLite database  
4. Backend server exposes alert data via REST API  
5. Dashboard fetches and displays alerts  

---

## ▶️ How to Run the Project

### 1️⃣ Run the analyzer
```bash
python analyzer.py
