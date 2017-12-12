import sys
import socket
from PyQt5 import QtWidgets, QtGui

#socket server info
hostMACAddress = '00:1f:e1:dd:08:3d' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
except:
    print("Closing socket")
    client.close()
    s.close()

#app info
def window():
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QWidget()
        l1 = QtWidgets.QLabel(w)
        b = QtWidgets.QPushButton(w)
        b.setText('Push Me')
        l1.setText('Hello World')
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(b)
        v_box.addWidget(l1)
        w.setWindowTitle('PyQt5 Lesson 2')
        w.setGeometry(200, 200, 300, 300)
        l1.move(152, 150)
        b.move(150,170)
        w.show()
        sys.exit(app.exec_())

window()
