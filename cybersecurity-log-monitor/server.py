from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/alerts":
            conn = sqlite3.connect("alerts.db")
            cursor = conn.cursor()

            cursor.execute("SELECT ip, alert_type, severity, description FROM alerts")
            rows = cursor.fetchall()
            conn.close()

            alerts = []
            for row in rows:
                alerts.append({
                    "ip": row[0],
                    "type": row[1],
                    "severity": row[2],
                    "description": row[3]
                })

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(alerts).encode())

        elif self.path == "/" or self.path == "/dashboard":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("dashboard.html", "rb") as f:
                self.wfile.write(f.read())

server = HTTPServer(("localhost", 8000), RequestHandler)
print("Server running at http://localhost:8000")
server.serve_forever()
