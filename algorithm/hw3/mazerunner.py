from maze import Maze

"""
    [과제 3]
        mazerunner.py 파일의 shortest_path() 함수를 완성하시오.
        이 파일 안에서 함수를 더 만들어도 괜찮지만, 주어진 함수의 매개변수는 건드리지 말 것
        maze.py, mazetester.py는 건드리지 말 것
    
    [올바른 경로valid path란?]
        (1, 1) 로 시작하지 않거나,
        (HEIGHT, WIDTH) 로 끝나지 않거나,
        이동 방향이 상하좌우 네 방향이 아니거나
        벽'#'이 포함된 경로는 유효하지 않은 경로 invalid path
        
    [경로 길이]
        편의상 "경로에 포함된 좌표 개수"로 정의함
        
    [제출]
        mazerunner.py
        
    [채점기준]
        invalid path이면 0점
        경로 길이가 최적해의 100%면 만점, (100+x)% 이면 점수는 (100-x)%
        즉, 경로 길이가 최적해의 두 배 이상이면 0점
        
        **웹에서 검색한 결과를 참고해서 작성한 경우 출처를 적어 둘 것
        평가에는 반영되지 않으나, 출처 표기 없이 유사한 코드가 발견되면 0점
"""

# 이 함수를 먼저 만들어보는 걸 추천함
# def shortest_path_length(maze):
    # maze에서 (1, 1)에서 (maze.height, maze.width)까지 가는 최단 경로의 "길이"를 리턴(정수)
    # 이동 방향은 상/하/좌/우 네 방향 (대각선x)
    # 갈 수 있는 경로가 없으면 -1을 리턴한다.
    # return -1

def tuple_sum(p, rand):
    return (p[0] + rand[0], p[1] + rand[1])

maze_sample = Maze(height=3, width=3, ratio=0.0)
mypath = [(1, 1)] # 시작점은 (1, 1)부터
p = (1, 1) # 현재위치
route = [(0, 1), (1, 0), (-1, 0), (0, -1)] # r, d, u, l

"""
    이동할 위치의 코드를 밑으로 내려서 수정해보면 될듯?
"""

def shortest_path(maze):
    global p, mypath, route
    for i in route:
        print(f"현재 위치 : {p}") # 현재 위치
        p = tuple_sum(p, i) # 현재 위치 업데이트
        mypath.append(p) # 경로 추가
        print(f"이동할 위치 : {p}")

        if maze.maze[p[0]][p[1]] == '#': # 만약 벽이라면,
            print("#")
            print(mypath)
            p = mypath[-2] # 현재 위치를 이전 위치로 변경
            mypath.pop() # 경로 삭제
            return
        else:
            if p in mypath:
                print("중복")
                print(mypath)
                p = mypath[-2] # 현재 위치를 이전 위치로 변경
                mypath.pop() # 경로 삭제
                shortest_path(maze)
                print("------")
            else:
                print("@") # 아니라면, 이동
                shortest_path(maze)

        
    if maze.width == p[0] and maze.height == p[1]:
        return mypath # 만약 현재 위치가 목적지라면 경로 반환
    else:
        return [] # 아니라면 빈 리스트 반환
    

    # 결론: 테스트는 여기서 해서 최적의 값을 구하고, 리턴값으로 [튜플]을 리턴하면됨.

    # print(maze.view_path([(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]))
    # maze에서 (1, 1)에서 (maze.height, maze.width)까지 가는 "최단 경로"를 리턴
    # 이동 방향은 상/하/좌/우 네 방향 (대각선x)
    # 경로는 2-tuple의 리스트로 만든다(예: [(1,1), (1, 2), (2, 2), ...]
    # 갈 수 있는 경로가 없으면 []를 리턴한다.

maze_sample.view_path(shortest_path(maze_sample))