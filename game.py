class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Essa posição já está ocupada. Escolha outra posição válida.")

    def check_winner(self):
        # Verificar linhas
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Verificar colunas
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Verificar diagonais
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        # Verificar empate
        if all(self.board[row][col] != " " for row in range(3) for col in range(3)):
            return "Empate"

        return None
