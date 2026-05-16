import pandas as pd
import serial
import time
from datetime import datetime, timedelta

EXCEL_FILE = r"D:\School\Scripting and Automation\FinalProject\assignments.xlsx"
PORT = "COM4"

def start_monitor():
    try:
        ser = serial.Serial(PORT, 115200, timeout=1)
        time.sleep(2)
        print("System Active.")
    except Exception as e:
        print(f"Connection Failed: {e}")
        return

    while True:
        try:
            df = pd.read_excel(EXCEL_FILE)
            now = datetime.now()
            active_idx = None

            # Logic Check
            for idx, row in df.iterrows():
                if str(row['Status']).strip().lower() != 'done':
                    deadline = pd.to_datetime(row['Deadline'])
                    if deadline <= (now + timedelta(hours=24)):
                        ser.write(b"ON\n")
                        active_idx = idx
                        break 
            else:
                ser.write(b"OFF\n")

            # Button Check
            if ser.in_waiting > 0:
                if "DONE" in ser.readline().decode('utf-8'):
                    if active_idx is not None:
                        df.at[active_idx, 'Status'] = 'Done'
                        df.to_excel(EXCEL_FILE, index=False)
                        print(f"Updated: {df.at[active_idx, 'Assignment']}")

        except PermissionError:
            print("Please close the Excel file.")
        
        time.sleep(5)

if __name__ == "__main__":
    start_monitor()