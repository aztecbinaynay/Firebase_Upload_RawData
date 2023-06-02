import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

ser = serial.Serial("COM6", 115200)

cred = credentials.Certificate(r"C:\Users\Q-5311\Desktop\john\credentials\copper-oven-382608-ea1f4baca1f3.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://copper-oven-382608-default-rtdb.asia-southeast1.firebasedatabase.app'
})

root = db.reference()

# Create a new data object to add
new_data = {
    0: 2
}

# Generate a server-side timestamp
timestamp = db.ServerValue.TIMESTAMP

# Add the new data with the timestamp key
root.child(str(timestamp)).set(new_data)

# Print the timestamp key
print("Timestamp key:", timestamp)

# try:
#     while True:
#         while True:
#             try:
#                 line = (
#                     ser.readline().decode().strip()
#                 )  # read the line from the serial port and decode it
#                 break
#             except UnicodeDecodeError:
#                 continue
#         values = line.split(
#             "\t"
#         )  # split the line into separate values using the tab character as a separator

#         if len(values) == 6:  # check if the number of values is correct
#             try:
#                 num1 = round(float(values[0]), 3)
#                 num2 = round(float(values[1]), 3)
#                 num3 = round(float(values[2]), 3)
#                 num4 = round(float(values[3]), 3)
#                 num5 = round(float(values[4]), 3)
#                 num6 = round(float(values[5]), 3)

#                 print(num1, num2, num3, num4, num5, num6)

#                 doc_ref.update({
#                     "AirFlow": firestore.ArrayUnion([num1]),
#                     "ECG": firestore.ArrayUnion([num2]),
#                     "HR": firestore.ArrayUnion([num3]),
#                     "Snore": firestore.ArrayUnion([num4]),
#                     "SpO2": firestore.ArrayUnion([num5]),
#                     "Therm": firestore.ArrayUnion([num6]),
#                 })

#             except ValueError:
#                 pass  # ignore any lines that cannot be parsed as float values
# finally:
#     users_ref = db.collection("users")
#     docs = users_ref.stream()
#     for doc in docs:
#         print(f"{doc.id} => {doc.to_dict()}")
