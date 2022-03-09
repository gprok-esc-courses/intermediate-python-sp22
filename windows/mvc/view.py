import sys

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QApplication, QWidget


class View:
    def __init__(self, controller):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(300, 300, 300, 500)
        self.window.setWindowTitle("Counter")
        layout = QVBoxLayout()
        self.label = QLabel("0")
        self.increase_btn = QPushButton("+")
        self.increase_btn.clicked.connect(controller.btn_increase_clicked)
        self.decrease_btn = QPushButton("-")
        self.decrease_btn.clicked.connect(controller.btn_decrease_clicked)
        layout.addWidget(self.label)
        layout.addWidget(self.increase_btn)
        layout.addWidget(self.decrease_btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.window.setCentralWidget(widget)

    def start(self):
        self.window.show()
        sys.exit(self.app.exec_())

    def update_counter_label(self, value):
        self.label.setText(str(value))