import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout


app = QApplication(sys.argv)

window = QWidget()
layout = QGridLayout()
layout.setSpacing(1)

window.setWindowTitle("TicTacToe")

for row in range(3):
    for col in range(3):
        b = QPushButton(str(row)+str(col))
        b.setFixedWidth(50)
        b.setFixedHeight(50)
        layout.addWidget(b, row, col, 1, 1)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

window.show()
sys.exit(app.exec_())