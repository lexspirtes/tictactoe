'''Lex Spirtes two-player tic tac toe game'''
from random import randint


def see_board(board):
    '''see_board() prints the current board in terminal
    '''
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])

'''list of winning sets'''    
winners = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def decide_players():
    '''decide_players() lets player1 decide whether they want to be X or O
    '''
    player1 = str(raw_input('Would Player 1 like to be X or O?'))
    if (player1 == "X" or player1 == 'O')== False:
        print("hey, that wasn't one of the options")
        play()
    else:
        if player1 == 'X':
            print("Okay, then player 2 is O")
            player2 = 'O'
            
        else:
            print("Okay, then player 2 is X")
            player2 = 'X'
    return (player1, player2)

def get_input(player, board):
    '''get_input(player, board): given a player and current board,
    tells inputs players move if valid, 
    if not valid (either space taken or not in board) lets player choose again 
    '''
    play = int(raw_input())
    if (board[play-1] == 'X' or board[play-1] == 'O') == True:
        print('that space is already full')
        get_input(player, board)
    elif (play-1 > 9 or play-1 < 0) == True:
        print("that's not even on the board!!")
        get_input(player, board)
    else:
        board[play -1] = player

def computer_move(board, player1):
    open_moves = []
    for b in range(0,len(board)):
        if board[b] == ' ':
            open_moves.append(b)
    place = randint(0, len(open_moves) -1)
    if player1 == 'X':
        board[open_moves[place]] = 'O'
    else:
        board[open_moves[place]] = 'X'
               
def check_board(player1, board):
    '''check_board(player1, board) checks the current board to see if someone has won a game. 
    If yes, returns the winner and asks to play again. If no, game continues
    '''
    for combo in winners:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == 'X':
            if player1 == 'X':
                print('Congrats player 1, you win!!')
            else:
                print('Congrats player 2, you win!!')
            see_board(board)
            play_again()
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] == 'O':
            if player1 == '0':
                print('Congrats Player 1, you win!!')
            else:
                print('Congrats Player 2, you win!!!')
            see_board(board)
            play_again()
        
def play_better():
    '''play_better() is the tic tac toe game, utilizing:
    see_board(board)
    play_again()
    get_input(player, board)
    check_board(player, board)
    random.randint()
    '''
    print("""Welcome to Tic Tac Toe! 
        This is a two player game, so first Player 1 will pick whether they're Xs or Os.
        Then you will start to play! 
        The board coordinates are 1-9 top left to bottom right. Good luck!!
        """)

    def player_loop(player_bool):
        '''player_loop(player_bool): given the player_bool, asks and 
        records that particular play
        '''
        print('~~~~~~~~~~~~~~~')
        if player_bool == True:
            p = 'Player 1'
            player = player1
            get_input(player,board)
        else:
            computer_move(board,player1)
        #    p = 'Player 2'
         #   player = player2
       # print(p + ':')
       # get_input(player, board)
        check_board(player, board)
        see_board(board)
        
    player1, player2 = decide_players()
    fate = randint(0,1)
    board = [' '] * 9
    count = 0
    p1turn = True
    see_board(board)
    if fate == 0:
        print("the fates have decided, Player 1 is starting")
    else:
        print("the fates have decided, Player 2 is starting")
        p1turn = False
    while count <= 9:
        if count == 9:
            print('this is a tie!')
            play_again()
        else:
            player_loop(p1turn)
            count += 1
            p1turn = not p1turn 

def play_again():
    '''play_again(): asks the player if they would like to play, if yes
    creates new game, if no, exits. 
    '''
    yorn = str(raw_input('would you like to play again? y/n'))
    if yorn == 'y':        
        play_better()
    else:
        print('goodbye')
        exit()
            
play_better()
