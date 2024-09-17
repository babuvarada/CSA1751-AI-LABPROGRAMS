class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                return True
            elif ' ' not in self.board:
                print("It's a tie!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        return False

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return False

    def play(self):
        while True:
            self.print_board()
            position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
            if 0 <= position < 9:
                if self.make_move(position):
                    self.print_board()
                    break
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
