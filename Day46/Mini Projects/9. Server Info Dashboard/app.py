import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    port = 8000
    env = os.environ.get("FLASK_ENV", "Not specified")
    debug = os.environ.get("FLASK_DEBUG", "0")
    
    print("Accessed: /")  # Console log
    return (
        f"IP Address: {ip_address}<br>"
        f"Port: {port}<br>"
        f"Environment: {env}<br>"
        f"Debug Mode: {'Enabled' if debug == '1' else 'Disabled'}"
    )

@app.route("/status")
def status():
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    print("Accessed: /status")  # Console log
    return "Running in Debug Mode" if debug_mode else "Running in Production Mode"

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Manually set port