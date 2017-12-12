import sys
import socket
from PyQt5 import QtWidgets, QtGui

#socket client info
serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
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
