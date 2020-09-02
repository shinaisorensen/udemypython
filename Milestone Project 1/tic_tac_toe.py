from random import randint

def display_board(board):
    print('')
    print(board[1:4])
    print(board[4:7])
    print(board[7:])
    
def choose_first_player():
    x = randint(1,2)
    
    if x == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def choose_mark():
    mark = ''
    
    while not (mark == 'X' or mark == 'O'):
        mark = input('Player 1 pick a mark, X or O: ').upper()
        
    if mark == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

def check_position(board, position):
    # Returns true if there is no mark on the position
    return not (board[position] == 'X' or board[position] == 'O')

def choose_position(board, player):
    position = ''
    
    while not (position in range(1,10)):
        position = input(f'{player}, pick a position from 1-9 to place your mark: ')
        
        if position.isdigit() and int(position) in range(1,10):
            if check_position(board, int(position)):
                return int(position)
            else:
                print('\nPlease enter another position.')

def place_marker(board, position, mark):
    board[position] = mark
    
def win_check(board, mark):
    # Total 3 marks to win the game
    win = 0

    # Rows
    rows = [board[1:4],board[4:7],board[7:]]

    # Columns
    columns = [[board[1], board[4], board[7]],[board[2], board[5], board[8]],[board[3], board[6], board[9]]]

    # Diagonals
    diags = [[board[3], board[5], board[7]],[board[1], board[5], board[9]]]

    for row in rows:
        for space in row:
            if not (space == mark):
                win = 0
            else:
                win += 1
        if win == 3:
            return True

    for column in columns:
        for space in column:
            if not (space == mark):
                win = 0
            else:
                win += 1 
        if win == 3:
            return True

    for diag in diags:
        for space in diag:
            if not (space == mark):
                win = 0
            else:
                win += 1
        if win == 3:
            return True

    return False

def check_full_board(board):
    # Returns false if there is still space on the board, true if full    
    for space in board[1:]:
        if not (space == 'X' or space == 'O'):
            return False
    return True

def replay():
    answer = ''
    
    while not (answer == 'Y' or answer == 'N'):
        answer = input('Would you like to continue? Y or N:').upper()
        print()
    
    return answer == 'Y'

while True:
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_on = True
    print('Let\'s play a game of Tic Tac Toe.')

    mark1, mark2 = choose_mark()
    print(f'\nPlayer 1 has chosen {mark1}')
    print(f'Player 2 will be {mark2}\n')
    
    player = choose_first_player()
    print(f'{player} is up first')
    
    while game_on:
        if player == 'Player 1':
            display_board(board)
            position = choose_position(board, player)
            
            place_marker(board, position, mark1)
            
            if win_check(board, mark1):
                display_board(board)
                print()
                print(f'{player} won the game!')
                game_on = False
            else:
                if check_full_board(board):
                    display_board(board)
                    print()
                    print('The game is a tie!')
                    game_on = False
                else:
                    player = 'Player 2'
        
        else:
            # Player 2
            display_board(board)
            position = choose_position(board, player)
            
            place_marker(board, position, mark2)
        
            if win_check(board, mark2):
                display_board(board)
                print()
                print(f'{player} won the game!')
                game_on = False
            else:
                if check_full_board(board):
                    display_board(board)
                    print()
                    print('The game is a tie!')
                    game_on = False
                else:
                    player = 'Player 1'
        
    if not replay():
        print('Thanks for playing!')
        break
    