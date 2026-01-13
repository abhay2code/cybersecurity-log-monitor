'''# analyzer.py
print("Cybersecurity Log Analyzer Started")

with open("logs.txt.txt", "r") as file:
    logs = file.readlines()

print("Total log entries:", len(logs))
'''
'''

# analyzer.py
print("Cybersecurity Log Analyzer Started\n")

failed_attempts = {}

with open("logs.txt.txt", "r") as file:
    logs = file.readlines()

for line in logs:
    if "FAILED_LOGIN" in line:
        parts = line.split()
        ip = parts[-1].split("=")[1]

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

print("Failed login attempts by IP:")
for ip, count in failed_attempts.items():
    print(ip, "→", count)

print("\n🚨 Suspicious IPs (Brute-force detected):")
for ip, count in failed_attempts.items():
    if count >= 5:
        print("ALERT:", ip, "with", count, "failed attempts")
'''

'''

# analyzer.py
print("Cybersecurity Log Analyzer Started\n")

failed_attempts = {}
successful_logins = []

with open("logs.txt.txt", "r") as file:
    logs = file.readlines()

for line in logs:
    parts = line.split()

    if "FAILED_LOGIN" in line:
        ip = parts[-1].split("=")[1]
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    if "SUCCESS_LOGIN" in line:
        ip = parts[-1].split("=")[1]
        successful_logins.append(ip)

print("Failed login attempts by IP:")
for ip, count in failed_attempts.items():
    print(ip, "→", count)

print("\nSuccessful logins:")
for ip in successful_logins:
    print(ip)

print("\n🚨 HIGH-RISK ALERTS (Success after brute-force):")
for ip in successful_logins:
    if failed_attempts.get(ip, 0) >= 5:
        print("CRITICAL ALERT:", ip, 
              "logged in successfully after",
              failed_attempts[ip],
              "failed attempts")

'''

# analyzer.py
import sqlite3

print("Cybersecurity Log Analyzer Started\n")

# Connect to database
conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

# Create alerts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    alert_type TEXT,
    severity TEXT,
    description TEXT
)
""")

failed_attempts = {}
successful_logins = []

with open("logs.txt.txt", "r") as file:
    logs = file.readlines()

for line in logs:
    parts = line.split()

    if "FAILED_LOGIN" in line:
        ip = parts[-1].split("=")[1]
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    if "SUCCESS_LOGIN" in line:
        ip = parts[-1].split("=")[1]
        successful_logins.append(ip)

# Brute-force alerts
for ip, count in failed_attempts.items():
    if count >= 5:
        cursor.execute(
            "INSERT INTO alerts (ip, alert_type, severity, description) VALUES (?, ?, ?, ?)",
            (ip, "Brute Force Attack", "HIGH", f"{count} failed login attempts detected")
        )

# Success after brute-force alerts
for ip in successful_logins:
    if failed_attempts.get(ip, 0) >= 5:
        cursor.execute(
            "INSERT INTO alerts (ip, alert_type, severity, description) VALUES (?, ?, ?, ?)",
            (ip, "Credential Compromise", "CRITICAL",
             f"Successful login after {failed_attempts[ip]} failed attempts")
        )

conn.commit()
conn.close()

print("🚨 Alerts successfully stored in database")
