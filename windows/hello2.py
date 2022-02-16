import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

def send_message():
    label.setText("Mouse Clicked!")

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

window.setWindowTitle("Hello App")
# window.setGeometry(100, 100, 600, 600)
label = QLabel('<h1>Hello World!</h1>')
layout.addWidget(label)
button = QPushButton('Click me')
button.clicked.connect(send_message)
layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

window.show()
sys.exit(app.exec_())