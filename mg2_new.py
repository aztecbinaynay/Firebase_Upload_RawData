import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import QEventLoop
import serial
from PyQt5.QtWidgets import QApplication

# Connect to the serial port
ser = serial.Serial("COM8", 115200)

# PyQtGraph
app = QApplication([])
win = pg.GraphicsLayoutWidget(show=True)
win.resize(800, 480)
plot_items = [win.addPlot(row=i, col=0) for i in range(0, 6)]
plot_curves = [plot_item.plot(pen=(i, 6)) for i, plot_item in enumerate(plot_items)]

# Set the y-axis range for the 5th graph
plot_items[4].setYRange(0, 100, padding = 0.2)
y_label = pg.TextItem("", anchor=(0, 1))
plot_items[4].addItem(y_label)


# Initialize data
max_length = 225
data = [np.zeros(max_length) for _ in range(6)]

# PyQtGraph
while True:
    while True:
        try:
            raw_data = (
                ser.readline().decode().strip()
            )  # read the line from the serial port and decode it
            break
        except UnicodeDecodeError:
            continue
    # Convert the data to a numpy array
    raw_data = raw_data.split("\t")
    if len(raw_data) == 6:
        new_data = np.array(raw_data).astype(float)
        new_data[4] = new_data[4].astype(int)
        print(new_data)
    else:
        continue

    # Append new data
    data = [np.append(d, nd)[-max_length:] for d, nd in zip(data, new_data)]

    # Update plot data
    for i, curve in enumerate(plot_curves):
        curve.setData(data[i])
        y_value = data[4][-1]
        y_label.setText(f"{y_value}")
        y_label.setPos(220, y_value-35)

        # create a text item for the y-axis label showing the values 10 seconds and 5 seconds ago.

        
        
    

    QApplication.processEvents(QEventLoop.AllEvents, 45)
