import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.red, 5, Qt.DotLine))
        painter.drawLine(10, 10, 300, 200)
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
        painter.drawEllipse(90, 100, 200, 90)
        painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()