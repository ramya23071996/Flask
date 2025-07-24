import os
from datetime import datetime

COMMON_PASSWORDS = {'123456', 'password', 'admin', 'qwerty', 'letmein'}

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def log_failed_login(ip, email):
    log_dir = os.path.join(os.path.dirname(__file__), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'login_attempts.log')
    with open(log_file, 'a') as f:
        f.write(f"[{datetime.now()}] Failed login attempt - Email: {email}, IP: {ip}\n")
