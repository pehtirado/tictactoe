from game import TicTacToeGame

def main():
    print("Bem-vindo ao Jogo da Velha!")
    print("Jogador 1: X")
    print("Jogador 2: O")
    print()

    game = TicTacToeGame()
    game.print_board()

    while not game.is_game_over():
        current_player = game.get_current_player()
        print(f"Jogador {current_player}, é sua vez.")
        row, col = get_player_move()
        while not game.make_move(row, col):
            print("Jogada inválida. Tente novamente.")
            row, col = get_player_move()

        game.print_board()
        print()

    result = game.get_game_result()
    if result == "X":
        print("Parabéns! O Jogador 1 (X) venceu!")
    elif result == "O":
        print("Parabéns! O Jogador 2 (O) venceu!")
    else:
        print("Empate!")

    print("Obrigado por jogar!")

def get_player_move():
    valid_input = False
    while not valid_input:
        try:
            row = int(input("Informe o número da linha (1, 2, 3): "))
            col = int(input("Informe o número da coluna (1, 2, 3): "))
            valid_input = True
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    return row, col

if __name__ == "__main__":
    main()
