from mazerunner import *
from mazerunneropt import *

"""
    과제 제출물을 평가하기 위한 코드
    참고용이므로 제출할 필요 없음
    과제 평가 시에는 별도로 생성한 sample.maze 파일을 사용함
"""

# Maze.save()로 저장해 둔 미로 불러오기
maze_sample = Maze.load("testcase/sample1_small.maze")
print(maze_sample)

# 랜덤 미로 생성하기
# maze_sample = Maze(height=3, width=3, ratio=0.0)
# maze_sample = Maze(height=5, width=5, ratio=0.0)
# maze_sample = Maze(height=5, width=5, ratio=0.2)
# maze_sample = Maze(height=10, width=8, ratio=0.3)
# maze_sample = Maze(height=30, width=20, ratio=0.3)
# print(maze_sample)
# print()

# 경로 길이만 구했을 때 확인해볼 수 있는 코드
# path_len = shortest_path_length(maze_sample)
# print('shortest path length =', path_len)
# print()
# exit(0)

# mypath = shortest_path(maze_sample)
# print('mypath =', mypath)
# print('length =', len(mypath))
#
# if mypath:
#     print('valid? =', maze_sample.is_valid_path(mypath))
#     print()
#     input('press enter to continue...')
#     maze_sample.view_path(mypath)


# 이 아래는 채점을 위한 코드
samples = [
    "sample1_small",
    "sample2_nopath",
    "sample3_medium",
    "sample4_nopath2",
    "sample5_large"]

print(*samples, sep=', ')

samples = [(name, Maze.load(name + ".maze")) for name in samples]
SCORE_PER_SAMPLE = 2.0
for name, maze in samples:
    score = 0.0
    opt_path = shortest_path_opt(maze)
    try:
        stu_path = shortest_path(maze)
        if not opt_path:
            if not stu_path:
                score = SCORE_PER_SAMPLE
            else:
                score = 0
        else:
            if not maze.is_valid_path(stu_path):
                score = 0
            else:
                stulen, optlen = len(stu_path), len(opt_path)
                stulen = min(stulen, optlen * 2)
                diff = stulen - optlen
                diff_ratio = diff / stulen
                score = SCORE_PER_SAMPLE * (1.0 - diff_ratio)
    except:
        score = 0

    print("%.3f" % score)

print()
