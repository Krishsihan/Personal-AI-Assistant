import os
import datetime

def open_app(app_name):
    os.system(f"open -a {app_name}")  # macOS
    return f"Opened {app_name}"

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def decide_tool(text):
    if "open" in text:
        return "open_app"
    if "time" in text:
        return "get_time"
    return None
