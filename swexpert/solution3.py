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

for i in range(1, T+1):
    buf = []
    top = []
    bottom = []
    left = []
    right = []
    # cnt = int(input())
    cnt = mcnt[i-1]
    for j in range(cnt):
        # mazes = list(map(int, input().split(" ")))
        mazes = list(map(int, maze[i-1][j].split(" ")))
        buf.append(mazes)
    # print(buf)
    for x in range(cnt):
        for y in range(cnt):
            if buf[x][y] == 1:
                # print(buf[x])
                for k in range(x, 0, -1):
                    if buf[x][y] == 1:
                        pass
                    buf[x][y] = 2
    print(buf)
    