import sys
from PyQt5 import QtWidgets, QtGui
#import bluetooth


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