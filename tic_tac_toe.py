##tic-tac-toe
print("Tic tac toe")

game_is_on = True
#who won or tie?
winner = None
current_player="X"

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

def creat_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3] + "|"+ board[4] + "|"+board[5])
    print(board[6] + "|"+board[7] + "|"+board[8] )



def play_game():
    #initial board display
    creat_board()

    #while game is played:
    while game_is_on:
            #enter the position from the random player:
            enter_posi(current_player)


            #check if game over
            check_game_over()
            #switch player
            switch_player()
    if winner=="X" or winner=="O":
        print(winner + "is winner" )
    elif winner==None:
        print("Tie")



def enter_posi(player):

    print(player+"'s turn ")
    position=input("Enter the position from 1-9 : ")
    valid=False
    while not valid:
     while position not in ["1","2","3","4","5","6","7","8","9"]:
        position=input("Invalid input .Choose from 1-9 Enter again :")
     position=int(position)-1

     if board[position]=="-":
        valid=True
     else:
        print("you cannot go again :")

    board[position]=player
    creat_board()



def check_game_over():
    check_if_win()
    check_if_tie()
    return

def check_if_win():
    '''check_columns:
    check_rows:
    check_diagonals:'''
    global winner
    row=check_rows()
    colomns=check_colomns()
    diag=check_diagonals()

    if row:
         winner=row
    elif colomns:
         winner=colomns
    elif diag:
         winner=diag
    else:
        winner=None


    return

def check_rows():
    global game_is_on
    row1= board[0]==board[1]==board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3 :
        game_is_on=False
    elif row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return  board[6]

    return

def check_colomns():

    global game_is_on
    col1= board[0]==board[3]==board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3 :
        game_is_on=False
    elif col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return  board[2]

    return


def check_diagonals():

    global game_is_on
    diag_1= board[0]==board[4]==board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2 :
        game_is_on=True
    elif diag_1:
        return board[0]
    elif diag_2:
        return board[2]

    return


def check_if_tie():
    global game_is_on
    global board
    if "-" not in board:
        game_is_on=False
    return



def switch_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return


play_game()