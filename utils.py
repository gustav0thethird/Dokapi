# utils.py

import datetime

def generate_csv_filename(scan_type, target):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_target = (
        target.replace("http://", "")
              .replace("https://", "")
              .replace("/", "_")
              .replace(":", "_")  # ✅ still replace colon for Windows safety
    )
    filename = f"dokapi_{scan_type}_{safe_target}_{date_time}.csv"
    return filename
