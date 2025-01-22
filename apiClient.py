import serial
import requests
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("PORT")
BAUDRATE = int(os.getenv("BAUDRATE"))
URL = os.getenv("URL")

ser = serial.Serial(PORT, BAUDRATE, timeout=1)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if line == "DETECTED":
            response = requests.get(URL)
            print(f"Wysłano żądanie: {response.status_code}")
