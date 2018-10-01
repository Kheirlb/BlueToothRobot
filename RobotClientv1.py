import sys
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtGui import QTextCursor
qtCreatorFile = "rawUI_v1.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#test change

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.connectBut.clicked.connect(self.connectDef)
        self.leftSl.valueChanged.connect(self.leftSlChange)

    def leftSlChange(self):
        self.history.insertPlainText("Speed is " + str(self.leftSl.value()) + '\n')
        self.history.moveCursor(QTextCursor.End)

    def connectDef(self):
        #print("Starting Connection...")
        self.history.insertPlainText("Starting Connection...\n")
        self.history.moveCursor(QTextCursor.End)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
