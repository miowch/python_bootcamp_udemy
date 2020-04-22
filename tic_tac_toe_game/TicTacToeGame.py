move_counter = 1
player1_symbol = ' '
player2_symbol = ' '
player_is_ready = True
player_is_winner = False
game_is_over = False
filled_cells = 0

board_grid = {
    'top': ' ___ ___ ___ ',
    'top_lines': '|   |   |   |',
    'board_values': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '},
    'left_side': '| ',
    'right_side': ' |',
    'separator': ' | ',
    'bottom_line': '|___|___|___|'
}

successful_sequences = [
    {7, 8, 9},
    {4, 5, 6},
    {1, 2, 3},
    {7, 4, 1},
    {8, 5, 2},
    {9, 6, 3},
    {7, 5, 3},
    {1, 5, 9}]


def choose_mark():
    global player1_symbol
    global player2_symbol

    print("Welcome to Tic Tac Toe!")
    player1_symbol = str(raw_input("Player 1: Do you want to be X or O? "))

    if player1_symbol.lower() == 'x':
        player2_symbol = 'o'
    else:
        player1_symbol = 'o'
        player2_symbol = 'x'
    print('Player 1 will go first.')


def print_board():
    def print_top_row():
        print(
                board_grid['left_side'] + board_grid['board_values'][7] + board_grid['separator'] +
                board_grid['board_values'][8] + board_grid['separator'] +
                board_grid['board_values'][9] + board_grid['right_side'])

    def print_middle_row():
        print(
                board_grid['left_side'] + board_grid['board_values'][4] + board_grid['separator'] +
                board_grid['board_values'][5] + board_grid['separator'] +
                board_grid['board_values'][6] + board_grid['right_side'])

    def print_bottom_row():
        print(
                board_grid['left_side'] + board_grid['board_values'][1] + board_grid['separator'] +
                board_grid['board_values'][2] + board_grid['separator'] +
                board_grid['board_values'][3] + board_grid['right_side'])

    print(board_grid['top'])
    print(board_grid['top_lines'])
    print_top_row()
    print(board_grid['bottom_line'])
    print(board_grid['top_lines'])
    print_middle_row()
    print(board_grid['bottom_line'])
    print(board_grid['top_lines'])
    print_bottom_row()
    print(board_grid['bottom_line'])


def ask_player_is_ready():
    global move_counter
    global player_is_ready
    global player1_symbol
    global player2_symbol
    global player_is_winner
    global game_is_over
    global board_grid
    global filled_cells

    if move_counter == 1:
        if str(raw_input('Are you ready to play? Enter Yes or No. ')).lower() == 'no':
            player_is_ready = False
            print('Then see you later!')
    else:
        if str(raw_input('Do you want to play again? Enter Yes or No. ')).lower() == 'no':
            player_is_ready = False
            print('Do you want to play again? Enter Yes or No: No.')
        else:
            move_counter = 1
            player_is_ready = True
            player_is_winner = False
            game_is_over = False
            filled_cells = 0
            for position in range(1, 10):
                board_grid['board_values'][position] = ' '


def make_move():
    global move_counter
    global filled_cells

    while True:
        position = int(raw_input('{}, choose your position? (1-9) '.format(active_player)))

        if board_grid['board_values'][position] != ' ':
            print('Oops! This cell is already taken.')
            continue
        else:
            board_grid['board_values'][position] = active_player_mark
            move_counter += 1
            filled_cells += 1
            break


def check_player_is_winner():
    global player_is_winner
    global game_is_over
    global filled_cells

    player_set = set()

    for cell in board_grid['board_values']:
        if board_grid['board_values'][cell] == active_player_mark:
            player_set.add(cell)

    for sequence in successful_sequences:
        hit = 0
        for number in sequence:
            if number in player_set:
                hit += 1
            if hit == 3:
                player_is_winner = True

    if filled_cells == 9 and hit != 3:
        game_is_over = True


choose_mark()
ask_player_is_ready()

while player_is_ready:
    print_board()
    if move_counter % 2 != 0:
        active_player = 'Player 1'
        active_player_mark = player1_symbol
    else:
        active_player = 'Player 2'
        active_player_mark = player2_symbol

    make_move()
    check_player_is_winner()
    print('\n' * 10)

    if player_is_winner:
        print_board()
        print "Congratulations! {} have won the game!".format(active_player)
        ask_player_is_ready()
        if not player_is_ready:
            break

    if game_is_over:
        print("Standoff!")
        ask_player_is_ready()
        if not player_is_ready:
            break
