# A function that will display the board
def show_board(board):
    printing_position = 1

    for i in board:

        if printing_position % 3 != 0:
            print(i, end=' ')
        else:
            print(i, end='\n')

        printing_position += 1

    print()


# A function that will print the rules
def show_rules():
    print('Choose a position, positions are given below')
    print('If you get X or O in a row or across, you win', end='\n')

    position_board = [i for i in range(1, 10)]
    show_board(position_board)


# A function that will clear console
def clear_console():
    print('\n' * 100)


# A function that will validate input
def valid_position(position):
    return 0 <= position <= 8


# A function that will update board
def update_board(board, position, symbol):
    if board[position] == '_':
        board[position] = symbol


# A function that will check for 3 in a row
def winner(board):
    # Row Check
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print('Player 2 has won the game')
        return True

    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        print('Player 2 has won the game')
        return True

    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        print('Player 2 has won the game')
        return True

    # Column Check
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        print('Player 2 has won the game')
        return True

    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print('Player 2 has won the game')
        return True

    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        print('Player 2 has won the game')
        return True

    # Diagonal Check
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        print('Player 2 has won the game')
        return True

    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        print('Player 1 has won the game')
        return True

    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        print('Player 2 has won the game')
        return True


# A function that will check whether a slot has been filled
def open_slot(board, pos):
    return board[pos] != 'X' and board != 'O'


# A function that will run the game infinite times
def multiple_times():
    game_runner()

    play_again = True

    while play_again:

        choice = input('\nWould you like to play again? Y or N\n')

        if choice == 'Y':
            print('New Game \n')
            game_runner()
        elif choice == 'N':
            print('Thank You for Playing')
            play_again = False
        else:
            pass


# A function that will run the game
def game_runner():
    show_rules()

    game_board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    show_board(game_board)

    slots_filled = 9

    while True:

        if winner(game_board):
            break

        elif slots_filled == 0:
            print('Its a Tie Game!')
            break

        p1_pos = int(input('Player 1 choose a position: '))
        p1_pos -= 1

        if valid_position(p1_pos) and open_slot(game_board, p1_pos):
            slots_filled -= 1

            update_board(game_board, p1_pos, 'X')

            show_board(game_board)
        else:

            valid_pos = False

            while not valid_pos:
                print('The position is incorrect! Try again')
                p1_pos = int(input('Player 1 choose a position: '))
                p1_pos -= 1

                if valid_position(p1_pos) and open_slot(game_board, p1_pos):

                    slots_filled -= 1

                    if winner(game_board):
                        break
                    elif slots_filled == 0:
                        print('Its a Tie Game!')
                        break

                    update_board(game_board, p1_pos, 'X')
                    show_board(game_board)
                    valid_pos = True

        if winner(game_board):
            break
        elif slots_filled == 0:
            print('Its a Tie Game!')
            break

        p2_pos = int(input('Player 2 choose a position: '))
        p2_pos -= 1

        if valid_position(p1_pos) and open_slot(game_board, p2_pos):
            slots_filled -= 1

            update_board(game_board, p2_pos, 'O')

            show_board(game_board)
        else:

            valid_pos = False

            while not valid_pos:
                print('The position is incorrect! Try again')
                p2_pos = int(input('Player 1 choose a position: '))
                p2_pos -= 1

                if valid_position(p1_pos) and open_slot(game_board, p2_pos):

                    slots_filled -= 1

                    if winner(game_board):
                        break
                    if slots_filled == 0:
                        print('Its a Tie Game!')
                        break

                    update_board(game_board, p2_pos, 'X')
                    show_board(game_board)
                    valid_pos = True


multiple_times()
