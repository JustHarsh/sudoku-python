# sudoku-python
Play sudoku with an interactive UI 


Step 1: User enters a board of their choice like so - 
```[[' ', ' ', ' ', 'B' ], [' ', 'B', ' ', ' ' ], [' ','C',' ','D' ], [' ', 'A', 'B', ' ']]```

Step 2: Display the board entered by the user - 
```     
     1 2 3 4
    +-+-+-+-+
   1|   |B  |
   2|B  |   |
    +-+-+-+-+
   3|C  |  D|
   4|A C|B  |
    +-+-+-+-+
  ```

Step 3: Ask user to enter a letter in the format: x-coordinate y-coordinate value. For example,
1 2 A. 

Step 4: Check if the input is valid using predefined rules (can be found below). If input is valid,
print the letter entered by the user on the board.

Step 5: After all the board is full, stop the game. 


# the "predefined rules" - 

```py 
def square_rule_violated(row, col, value):
```
The ```square_rule_violated()``` function checks if there is a duplication of letters in the nearest surrounding of its place on the board. 
For example, 

```
  1 2 3 4
 +-+-+-+-+
1|   |B  |
2|B  |   |
 +-+-+-+-+
3|C  |  D|
4|A C|B  |
 +-+-+-+-+
 ```

The square rule is violated in the example above because C at (4,2) is one of the nearest neighbours of
C at (3,1). However, the below would NOT be an example of this violation.

```
  1 2 3 4
 +-+-+-+-+
1|   |B  |
2|B  |   |
 +-+-+-+-+
3|  C|C D|
4|A  |B  |
 +-+-+-+-+
```

Here, C at (3,3) does NOT violate the square rule because it is not in its local square coordinates i.e., nearest 
neighbour, [(3,1), (3,2), (4,1), (4,2)].

Hence, if the square rule is violated, the function returns True.

```py
def vertical_rule_violated(row, col, value):
```

The ```vertical_rule_violated()``` fucntion checks if there is a duplication of letters along a vertical line on the board, then function returns True, else it
returns False.


```py
def horizontal_rule_violated(row, col, value):
```

The ```horizotal_rule_violated()``` fucntion checks if there is a duplication of letters along a horizontal line on the board, then function returns True, else it
returns False.


```py
def all_cells_filled():
```

The ```all_cells_filled()``` function checks if the entire board is filled. Returns True when there is no coordinate is " ".

Once all cells are filled, the game stops and prints ```Good game!``` in the console. 
