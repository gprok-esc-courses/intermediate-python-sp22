from player import Player
from board import Board


class Game:
    def __init__(self):
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.current_player = self.player_x
        self.board = Board()

    def run_game(self):
        # loop until win or tie
        while True:
            self.board.display()
            # ask current player to play
            print(self.current_player.symbol + " plays")
            row, col = self.current_player.play()
            # play whatever he selected in board
            ok = self.board.play(row, col, self.current_player.symbol)
            if ok:
                # check for win, if yes stop
                winner = self.board.winner()
                if winner is not None:
                    print(winner + " wins!")
                    # add score to the winner
                    break
                # check for tie, if yes stop
                if self.board.tie():
                    print("It's a Tie!")
                    break;
                self.current_player = self.player_o if self.current_player == self.player_x else self.player_x
        # ask to play again
            # init new game



game = Game()
game.run_game()