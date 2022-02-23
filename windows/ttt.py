import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout


app = QApplication(sys.argv)

window = QWidget()
button_layout = QGridLayout()
button_layout.setSpacing(1)

window.setWindowTitle("TicTacToe")

for row in range(3):
    for col in range(3):
        b = QPushButton(str(row)+str(col))
        b.setFixedWidth(50)
        b.setFixedHeight(50)
        button_layout.addWidget(b, row, col, 1, 1)

button_widget = QWidget()
button_widget.setLayout(button_layout)

window.setCentralWidget(button_widget)
window.show()
sys.exit(app.exec_())

window.show()
sys.exit(app.exec_())