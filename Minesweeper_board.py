import random  #for randomly placing mines

rows = 10 #creating 10x10 board with 10 mines
columns = 10
mine_count = 10

board = [[0 for i in range(0, rows)] for j in range(0, columns)] #creating the actual board, each position initialized to 0 at first

board_coordinates = [(x, y) for x in range(0,columns) for y in range(0, rows)] #setting all possible board coordinates
mine_coordinates = random.sample(board_coordinates, mine_count) #randomly selecting 10 coordinates for mines

for mine in mine_coordinates: #placing mines and marking them with "10"
    x,y = mine
    board[x][y] = 10
    neighbors = [(x-1,y),(x-1,y+1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y-1)] #updating neighbors after mines are placed
    for n in neighbors: #checks neighbors' validity and updates values if it is by a mine
        if 0 <= n[0] <= columns-1 and 0 <= n[1] <= rows-1 and n not in mine_coordinates:
            board[n[0]][n[1]] += 1

starting_point = (0,0) #creating the starting point
board_coordinates = [(x, y) for x in range(0,columns) for y in range(0, rows) if (x,y) != starting_point] #regenerates coordinates
def get_mine_neighbors(x,y): #defining coordinates of surrounding cells
    mines = []
    neighbors = [(x-1,y),(x-1,y+1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y-1)]
    for n in neighbors: #finds and returns coordinates of neighboring mines
        if 0 <= n[0] <= columns-1 and 0 <= n[1] <= rows-1:
            if board[n[0]][n[1]] == 10:
                mines.append(n)
    return mines

for i in range(0,columns): #checks mine counts
    for j in range(0,rows):
        sq = board[i][j]
        if sq > 0 and sq < 10:
            mine_neighbors = get_mine_neighbors(i,j)
            if sq != len(mine_neighbors): #error checking for valid number of mines
                print("not consistent!")

def print_board(board): #printing minesweeper board
    for row in board:
        row_display = ""
        for cell in row:
            if cell == 10:
                row_display += "◉ "
            else:
                row_display += str(cell) + " "
        print(row_display)

print_board(board)

