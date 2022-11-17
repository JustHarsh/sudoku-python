'''
Sudoku game - 

Step 1: User enters a board of their choice like so - 
[[' ', ' ', ' ', 'B' ], [' ', 'B', ' ', ' ' ], [' ','C',' ','D' ], [' ', 'A', 'B', ' ']]

Step 2: Display the board entered by the user - 
     1 2 3 4
    +-+-+-+-+
   1|   |B  |
   2|B  |   |
    +-+-+-+-+
   3|C  |  D|
   4|A C|B  |
    +-+-+-+-+

Step 3: Ask user to enter a letter in the format: x-coordinate y-coordinate value. For example,
1 2 A. 

Step 4: Check if the input is valid using predefined rules (can be found below). If input is valid,
print the letter entered by the user on the board.

Step 5: After all the board is full, stop the game. 
'''

def square_rule_violated(row, col, value):
    '''
    checks if there is a duplication of letters in the nearest surrounding of its place on the board. 
    For example, 

     1 2 3 4
    +-+-+-+-+
   1|   |B  |
   2|B  |   |
    +-+-+-+-+
   3|C  |  D|
   4|A C|B  |
    +-+-+-+-+

    The square rule is violated in the example above because C at (4,2) is one of the nearest neighbours of
    C at (3,1). However, the below would NOT be an example of this violation.

     1 2 3 4
    +-+-+-+-+
   1|   |B  |
   2|B  |   |
    +-+-+-+-+
   3|  C|C D|
   4|A  |B  |
    +-+-+-+-+

    Here, C at (3,3) does NOT violate the square rule because it is not in its local square coordinates i.e., nearest 
    neighbour, [(3,1), (3,2), (4,1), (4,2)].

    Hence, if the square rule is violated, the function returns True. 
    '''

    if (row-1) % 2 == 0 and (col-1) < 2:
      if value == board[row-1][0] or value == board[row-1][1] or value == board[row][1] or value == board[row][0]:
        return True
    elif (row-1) == 0 and (col-1) > 2:
      if value == board[0][2] or value == board[0][3] or value == board[1][2] or value == board[1][3]:
        return True

    elif (row-1) % 2 != 0 and (col-1) < 2:
      if value == board[row-1][0] or value == board[row-1][1] or value == board[row-2][1] or value == board[row-2][0]:
        return True
    elif (row-1) % 2 != 0 and (col-1) > 2:
      if value == board[row-1][2] or value == board[row-1][3] or value == board[row-2][2] or value == board[row-2][3]:
        return True

    return False 


def horizontal_rule_violated(row, col, value):
    '''
    if there is a duplication of letters along a horizontal line on the board, then function returns True, else it 
    returns False. 
    '''

    if value in board[row-1]:
      return True

    return False


def vertical_rule_violated(row, col, value):
    '''
    if there is a duplication of letters along a vertical line on the board, then function returns True, else it
    returns False. 
    '''

    for i in range(0,4):
      if value in board[i][col-1]:
        return True

    return False

def fstrip(string):
    '''remove ALL whitespaces in a string.'''
    return string.replace(" ", "")

def all_cells_filled():
    '''to check if the entire board is filled. Returns True when there is no coordinate is " ".'''

    if " " not in board[0] and " " not in board[1] and " " not in board[2] and " " not in board[3]:
        return True

board = eval(input("Enter your 2-d board (4x4): "))
game_on = True

# example board - [[' ', ' ', ' ', 'B' ], [' ', 'B', ' ', ' ' ], [' ','C',' ','D' ], [' ', 'A', 'B', ' ']]

def display_board():
    '''to display the board entered by the user.'''

    print('  {:2}{:2}{:2}{:2}'.format(
        1, 2, 3, 4
    ))

    print('  {:2}{:2}{:2}{:3}'.format(
        '+-', '+-', '+-', '+-+'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        1, '|', board[0][0], board[0][1],
        '|', board[0][2], board[0][3], '|'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        2, '|', board[1][0], board[1][1],
        '|', board[1][2], board[1][3], '|'
    ))

    print('  {:2}{:2}{:2}{:3}'.format(
        '+-', '+-', '+-', '+-+'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        3, '|', board[2][0], board[2][1],
        '|', board[2][2], board[2][3], '|'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        4, '|', board[3][0], board[3][1],
        '|', board[3][2], board[3][3], '|'
    ))

    print('  {:2}{:2}{:2}{:3}'.format(
        '+-', '+-', '+-', '+-+'
    ))

display_board()


while game_on:

    try:
      '''When the input is valid, try to insert the value entered by the user on the board if no rule is violated.'''

      attempt = input("Type a row number, a column number, and a letter (e.g., 1 2 A): ")
      
      attempt_cleaned = tuple(fstrip(attempt)) # tuple(fstrip(attempt)) = ("1", "2", "A")
      x = int(attempt_cleaned[0]) # row
      y = int(attempt_cleaned[1]) # col
      val = attempt_cleaned[2] # value

      PURPLE = "\033[0;35m"
      NORMAL = "\033[0m"
    
      if square_rule_violated(x, y, val):
          print("Square rule violated! Try again.")
          display_board()

      elif vertical_rule_violated(x, y, val):
          print("Vertical rule violated! Try again.")
          display_board()
        
      elif horizontal_rule_violated(x, y, val):
          print("Horizontal rule violated! Try again.")
          display_board()        

      else:
          board[x-1][y-1] = PURPLE + val + NORMAL
          display_board()

    except:
      '''
      if user input is invalid, i.e. coordinates are wrong or are not integers, run the except block 
      to keep the game running. 
      '''

      print("Invalid input.")
      display_board()

    finally:
      '''
      finally, after each try or except round, check if all cells are filled. If yes, print "Good game!" and 
      stop the game. 
      '''

      if all_cells_filled():
          print("Good game!")
          game_on = False