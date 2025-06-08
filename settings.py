import os
import datetime
from utils import generate_csv_filename     

class Settings:
    csv_output_enabled = False
    csv_output_directory = "./Reports"

    @classmethod
    def ensure_reports_folder(cls):
        os.makedirs(cls.csv_output_directory, exist_ok=True)

def generate_csv_filename(scan_type, target):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    safe_target = target.replace("http://", "").replace("https://", "").replace("/", "_")
    filename = f"dokapi_{scan_type}_{safe_target}_{date}.csv"
    return filename
