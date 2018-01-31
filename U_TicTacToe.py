
from IPython.display import clear_output
from sys import exit

#NOTE: Global variables
mark1 = 'X'
mark2 = 'O'

board_position = ['1', '2', '3', '4', '5', '6', '7', '8' , '9']
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def render_board():
    clear_output()
    print(board[6], "|", board[7], "|", board[8])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[0], "|", board[1], "|", board[2])
    print()
    print()

def assign_marker():
    global mark1
    global mark2

    mark1 = input('Player 1 enter your marker: ')
    if mark1.isalpha() == False:
         while not mark1.isalpha():
             mark1 = input('Player 1 re-enter your marker as a string: ')

    mark2 = input('Player 2 enter your marker: ')
    if mark2.isalpha() == False:
         while not mark2.isalpha():
              mark2 = input('Player 2 re-enter your marker as a string: ')

def turn_phase(marker):

    #NOTE: Marker turn and check for int
    print("It's ", marker, "'s turn.")
    cont = False
    turn = ''

    #NOTE: Place marker on board
    while cont == False:
         if turn == board_position[0]:
             board[0] = marker
             cont = True
         elif turn == board_position[1]:
             board[1] = marker
             cont = True
         elif turn == board_position[2]:
             board[2] = marker
             cont = True
         elif turn == board_position[3]:
             board[3] = marker
             cont = True
         elif turn == board_position[4]:
             board[4] = marker
             cont = True
         elif turn == board_position[5]:
             board[5] = marker
             cont = True
         elif turn == board_position[6]:
             board[6] = marker
             cont = True
         elif turn == board_position[7]:
             board[7] = marker
             cont = True
         elif turn == board_position[8]:
             board[8] = marker
             cont = True
         else:
              turn = input("Using the number pad, choose a position: ")

#NOTE: Check for winner
def win(marker):
     #NOTE: Checks for horizontal winner
     if board[6] == board[7] == board[8] == marker:
         print('You won! Good job!')
         play_again()

     if board[3] == board[4] == board[5] == marker:
         print('You won! Good job!')
         play_again()

     if board[0] == board[1] == board[2] == marker:
         print('You won! Good job!')
         play_again()

     #NOTE: Check for vertical winner
     if board[6] == board[3] == board[0] == marker:
         print('You won! Good job!')
         play_again()

     if board[7] == board[4] == board[1] == marker:
         print('You won! Good job!')
         play_again()

     if board[8] == board[5] == board[2] == marker:
         print('You won! Good job!')
         play_again()

     #NOTE: Check for diagonal winner
     if board[6] == board[4] == board[2] == marker:
         print('You won! Good job!')
         play_again()

     if board[8] == board[4] == board[0] == marker:
         print('You won! Good job!')
         play_again()

#NOTE: Play again?
def play_again():
     ans = input("Would you like to play again? yes or no ")
     if ans == "yes":
            board[0] = " "
            board[1] = " "
            board[2] = " "
            board[3] = " "
            board[4] = " "
            board[5] = " "
            board[6] = " "
            board[7] = " "
            board[8] = " "
            turnCount = 0
            play()

     elif ans == "no":
            exit()

     else:
            print("You didn't answer yes or no... I'm closing.")
            exit()

#NOTE: Game loop
def play():
    turnCount = 0
    gameLoop = True

    while gameLoop == True:
        assign_marker()

        #NOTE: Turn loop
        while turnCount != 8:
            render_board()
            turn_phase(mark1)
            render_board()
            win(mark1)
            turnCount += 1
            turn_phase(mark2)
            render_board()
            win(mark2)
            turnCount += 1
        print('Looks like there was a tie.')
        play_again()

#NOTE: Game Start
play()
