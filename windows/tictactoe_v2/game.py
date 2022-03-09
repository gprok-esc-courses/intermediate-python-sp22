from windows.tictactoe_v2.board import Board
from windows.tictactoe_v2.player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.px = Player("X", 1)
        self.po = Player("O", 2)
        self.current = self.px

    def update_score(self, winner_value):
        if self.px.value == winner_value:
            self.px.value += 1
        else:
            self.po.value += 1

    def play(self):
        pass