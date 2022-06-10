T = 1
# T = int(input())

mcnt = [7, 9, 11, 4]
maze = [["0 0 1 0 0 0 0",
         "0 0 1 0 0 0 0",
         "0 0 0 0 0 1 0",
         "0 0 0 0 0 0 0",
         "1 1 0 1 0 0 0",
         "0 1 0 0 0 0 0",
         "0 0 0 0 0 0 0"],
        
        ["0 0 0 0 0 0 0 0 0",
         "0 0 1 0 0 0 0 0 1",
         "1 0 0 0 0 0 0 0 0",
         "0 0 0 1 0 0 0 0 0",
         "0 1 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 1 0 0",
         "0 0 0 1 0 0 0 0 0",
         "0 0 0 0 0 0 0 1 0",
         "0 0 0 0 0 0 0 0 1"],

        ["0 0 1 0 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 0 0 0 0 1",
         "0 0 0 1 0 0 0 0 1 0 0",
         "0 1 0 1 1 0 0 0 1 0 0",
         "0 0 0 0 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 0 1 0 0 0",
         "0 0 0 0 0 0 0 0 0 0 0",
         "0 0 0 0 0 0 0 0 1 0 0",
         "0 0 0 0 0 0 1 0 0 0 0",
         "0 0 0 0 0 0 0 0 0 0 0"],
         
         ["1 1 1 1 1"
          "1 1 0 0 1"
          "0 0 0 1 1"
          "0 0 0 1 1"
          "1 0 1 1 1"]]

for i in range(T):
    ####################  Maze Data Initalize  #####################
    buffer = []
    for j in range(mcnt[i]):
        buffer.append(list(map(int, maze[i][j].split(" "))))
    print(buffer)
    ################################################################
    MIN_INDEX = 0
    MAX_INDEX = len(buffer)-1
    for x in range(MAX_INDEX):
        for y in range(MAX_INDEX):
            if buffer[x][y] == 1:
                if x == MIN_INDEX or x == MAX_INDEX or y == MIN_INDEX or y == MAX_INDEX:
                    pass
                    buffer[x][y] = 2

    print(buffer)