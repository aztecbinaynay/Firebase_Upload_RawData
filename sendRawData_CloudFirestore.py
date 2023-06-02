import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

ser = serial.Serial("COM6", 115200)

try:
    pass
    # while True:
    #     while True:
    #         try:
    #             line = (
    #                 ser.readline().decode().strip()
    #             )  # read the line from the serial port and decode it
    #             break
    #         except UnicodeDecodeError:
    #             continue
    #     values = line.split(
    #         "\t"
    #     )  # split the line into separate values using the tab character as a separator

    #     if len(values) == 6:  # check if the number of values is correct
    #         try:
    #             num1 = round(float(values[0]), 3)
    #             num2 = round(float(values[1]), 3)
    #             num3 = round(float(values[2]), 3)
    #             num4 = round(float(values[3]), 3)
    #             num5 = round(float(values[4]), 3)
    #             num6 = round(float(values[5]), 3)

    #             print(num1, num2, num3, num4, num5, num6)

    #         except ValueError:
    #             pass  # ignore any lines that cannot be parsed as float values
finally:

    cred = credentials.Certificate(r"C:\Users\Q-5311\Desktop\john\credentials\copper-oven-382608-ea1f4baca1f3.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection("users").document("xnSSNwkYrEduqQoEY0H0")

    
    doc_ref.set({
                    "AirFlow":[32,5,6,6],
                    "ECG": [32,5],
                    "HR": [32,5,6,6],
                    "Snore": [32,5,6,6],
                    "SpO2": [32,5,6,6],
                    "Therm": [32,5,6,6],
                })

    users_ref = db.collection("users")
    docs = users_ref.stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
