import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello App")
window.setGeometry(100, 100, 600, 600)
label = QLabel('<h1>Hello World!</h1>', parent=window)

window.show()
sys.exit(app.exec_())

