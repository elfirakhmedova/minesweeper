import random  #for randomly placing mines

rows = 10 #creating 10x10 board with 10 mines
columns = 10
mine_count = 10

board = [[0 for i in range(0, rows)] for j in range(0, columns)] #creating the actual board

board_coordinates = [(x, y) for x in range(0,columns) for y in range(0, rows)] #setting board coordinates
mine_coordinates = random.sample(board_coordinates, mine_count) #randomly setting coordinates for mines

for mine in mine_coordinates: #iterate through each mine
    x,y = mine
    board[x][y] = 10
    neighbors = [(x-1,y),(x-1,y+1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y-1)]
    for n in neighbors:
        if 0 <= n[0] <= columns-1 and 0 <= n[1] <= rows-1 and n not in mine_coordinates:
            board[n[0]][n[1]] += 1