from maze import Maze
import copy

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

def tuple_sub(p, rand):
    return (p[0] - rand[0], p[1] - rand[1])

maze_sample = Maze(height=8, width=8, ratio=0.3)
mypath = [(1, 1)] # 시작점은 (1, 1)부터
p = (1, 1) # 현재위치
route = [(0, 1), (1, 0), (0, -1), (-1, 0)] # r, d, l, u

def shortest_path(maze):
    global p, mypath, route
    real_p = p
    print(f"현재 위치 : {p}") # 현재 위치
    for i in route:
        p = tuple_sum(p, i) # 이동할 위치 업데이트
        print(f"이동할 위치 : {p}")

        if maze.maze[p[0]][p[1]] == '#': # 이동할 위치가 만약 벽이라면,
            print("#")
            p = real_p # 현재 위치를 이전 위치로 변경
        else: # 벽이 아니라면
            """
                이동 해야함, 근데 이미 이동 했던 곳이라면 이동하지 않음
                이부분 수정 필요
                shortest_path(maze) 
            """

        
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

success_path = []
def shortest_path2(maze, path=[(1, 1)], depth=0):
    global success_path
    # 경로(path)에서의 가장 마지막이 현재 위치
    p = path[-1]
    #print(f"현재 위치 : {p}") # 현재 위치
    if maze.maze[p[0]][p[1]] == '#':
        #print("여기는 벽임")
        return []
    # 목표 지점에 도착한 경우 현재까지의 경로를 반환
    if p == (maze.height, maze.width):
        return path
    # 하, 우, 좌, 상 이동 분기
    for i in route:
        # 이동할 위치 업데이트
        np = tuple_sum(p, i)
        #print(f"이동할 위치 : {np}")
        # 만약 이동할 위치가 경로에 포함된 경우 가지 않음
        if np in path:
            continue
        # 이동할 stack 에 새로운 경로 p 추가하여 새로운 분기 시작
        new_path = copy.deepcopy(path)
        new_path.append(np)
        find = shortest_path2(maze, new_path, depth + 1)
        # find 탐색에 성공한 경우 길이가 1보다 큼
        if len(find) > 0:
            if depth > 0:
                if success_path == [] or len(success_path) > len(find):
                    success_path = find
    if depth > 0:
        return []
    # 성공적인 경로를 출력
    print(success_path)

# maze_sample.view_path(shortest_path2(maze_sample))
print(maze_sample)
shortest_path2(maze_sample)

SCORE_MAX = 1000
optimal_solution = success_path

assert maze_sample.is_valid_path(success_path), "INVALID PATH"
assert maze_sample.is_valid_path(optimal_solution), "INVALID OPTIMAL PATH"

mylen, optlen = len(success_path), len(optimal_solution)

mylen = min(mylen, optlen * 2)
diff = mylen - optlen
diff_ratio = diff / mylen

myscore = SCORE_MAX * (1 - diff_ratio)
print(myscore)
maze_sample.view_path(success_path)
