
def print_win(player, direction):
    print(f"Player {player} is the winner {direction}!")

def win_row(row,direction):
    #print(row)
    if row.count(row[0]) == len(row) and row[0]!= 0:
        print_win(row[0],direction)
        return True
    return False

def win(current_game):
    has_won = False
    # check rows
    for row in current_game:
       has_won= has_won or win_row(row, "horizontally")
    # check colums
    for col in range(len(current_game[0])):
       has_won = has_won or win_row([row[col] for row in current_game],"vertically")
    #diag 1
    has_won = has_won or win_row([current_game[i][i] for i in range(len(current_game))],"diag1")
    #diag 2
    has_won = has_won or win_row([current_game[i][-1-i] for i in range(len(current_game))],"diag2")
    return has_won

def game_board(player = -1,row = 0, column=0 ):
    if(game[row][column] != 0):
        print("Position ocopado, try another one")
        return False
    if not player == -1:
        game[row][column]= player
    print("(    a  b  c")

    for count, row in enumerate(game):
        print(count,row)
        count +=1
    return True

keep_playing = True
current_player = 1

while(keep_playing):
    game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
    has_won = False
    game_board()
    while not has_won:
        print(f"Player {current_player}:")
        col_choice = int(input("Input column: "))
        row_choice = int(input("Input row: "))
        
        valid_play = game_board(current_player,row_choice,col_choice)
        if valid_play:
            has_won = win(game)
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1