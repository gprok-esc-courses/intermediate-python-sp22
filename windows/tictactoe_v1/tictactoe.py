import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QGridLayout, QPushButton, QWidget, QLabel, \
    QVBoxLayout


current_player = 'X'
score_x = 0
score_o = 0


def btn_play(button):
    global current_player
    button.setText(current_player)
    button.setEnabled(False)
    current_player = 'X' if current_player == 'O' else 'O'
    status_bar.showMessage(current_player + " plays")
    w = check_winner()
    if w == '':
        check_tie()

def check_winner():
    global buttons, score_o, score_x
    winner = ''
    if buttons[0].text() == buttons[1].text() and buttons[0].text() == buttons[2].text() and buttons[0].text() != '-':
        winner = buttons[0].text()
    if buttons[3].text() == buttons[4].text() and buttons[3].text() == buttons[5].text() and buttons[3].text() != '-':
        winner = buttons[3].text()
    if buttons[6].text() == buttons[7].text() and buttons[6].text() == buttons[8].text() and buttons[6].text() != '-':
        winner = buttons[6].text()
    if buttons[0].text() == buttons[3].text() and buttons[0].text() == buttons[6].text() and buttons[0].text() != '-':
        winner = buttons[0].text()
    if buttons[1].text() == buttons[4].text() and buttons[1].text() == buttons[7].text() and buttons[1].text() != '-':
        winner = buttons[1].text()
    if buttons[2].text() == buttons[5].text() and buttons[2].text() == buttons[8].text() and buttons[2].text() != '-':
        winner = buttons[2].text()
    if buttons[0].text() == buttons[4].text() and buttons[0].text() == buttons[8].text() and buttons[0].text() != '-':
        winner = buttons[0].text()
    if buttons[2].text() == buttons[4].text() and buttons[2].text() == buttons[6].text() and buttons[2].text() != '-':
        winner = buttons[2].text()
    if winner != '':
        status_bar.showMessage(winner + " WINS!")
        if winner == 'X':
            score_x += 1
        else:
            score_o += 1
        for b in buttons:
            b.setEnabled(False)
        score_label.setText("Score: X " + str(score_x) + " - O " + str(score_o))
    return winner


def check_tie():
    global buttons
    for b in buttons:
        if b.text() == '-':
            return
    status_bar.showMessage("It's a TIE!")

def play_again():
    global buttons, current_player
    for b in buttons:
        b.setText("-")
        b.setEnabled(True)
    status_bar.showMessage("X plays")
    current_player = 'X'

app = QApplication(sys.argv)

current_player = 'X'
score_x = 0
score_o = 0

window = QMainWindow()
window.setGeometry(300, 300, 300, 500)
window.setWindowTitle("TicTacToe v.1")

layout = QVBoxLayout()

button_layout = QGridLayout()
button_layout.setSpacing(1)

window.setWindowTitle("TicTacToe")

buttons = []
for row in range(3):
    for col in range(3):
        b = QPushButton("-")
        b.setFixedWidth(150)
        b.setFixedHeight(150)
        b.clicked.connect(lambda state, btn=b: btn_play(btn))
        buttons.append(b)
        button_layout.addWidget(b, row, col, 1, 1)

button_widget = QWidget()
button_widget.setLayout(button_layout)

score_label = QLabel("Score: X 0 - O 0")

play_again_btn = QPushButton("Play Again")
play_again_btn.clicked.connect(play_again)

layout.addWidget(score_label)
layout.addWidget(button_widget)
layout.addWidget(play_again_btn)

central_widget = QWidget()
central_widget.setLayout(layout)

status_bar = QStatusBar()
window.setStatusBar(status_bar)
status_bar.showMessage("X plays")

window.setCentralWidget(central_widget)
window.show()
sys.exit(app.exec_())